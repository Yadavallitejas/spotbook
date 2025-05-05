from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubCategoryForm
from .models import SubCategory, WorkerProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserSignupForm, WorkerSignupForm, LoginForm
from .models import Category, WorkerProfile, Booking, Message
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.http import require_GET

def create_subcategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')  # Redirect to a relevant view after saving
    else:
        form = SubCategoryForm()
    return render(request, 'create_subcategory.html', {'form': form})

def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(request, 'subcategory_list.html', {'subcategories': subcategories})

def get_workers_for_category(request, category_id):
    workers = WorkerProfile.objects.filter(categories__id=category_id)

    return render(request, 'workers_popup.html', {'workers': workers})


def home(request):
    categories = Category.objects.all()[:4]
    subcategories = SubCategory.objects.all()  # Fetch all subcategories

    return render(request, 'home.html', {'categories': categories, 'subcategories': subcategories})  # Pass subcategories to the template

def services(request):
    query = request.GET.get('q', '')
    if query:
        categories = Category.objects.filter(name__icontains=query)
        subcategories = SubCategory.objects.filter(name__icontains=query)
    else:
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()  # Fetch all subcategories

    return render(request, 'services.html', {'categories': categories, 'subcategories': subcategories, 'query': query})  # Pass subcategories to the template

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'term.html')
def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form, 'type': 'User'})

def worker_signup(request):
    if request.method == 'POST':
        form = WorkerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            worker_profile = WorkerProfile.objects.create(user=user)
            worker_profile.categories.set(form.cleaned_data['categories'])

            login(request, user)
            return redirect('home')
    else:
        form = WorkerSignupForm()
    return render(request, 'signup.html', {'form': form, 'type': 'Worker'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-id')
    return render(request, 'user_dashboard.html', {'bookings': bookings})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def book_service(request, category_id, subcategory_id=None):
    if subcategory_id:
        from .models import SubCategory
        subcategory = get_object_or_404(SubCategory, id=subcategory_id)
        category = subcategory.category  # Use parent category of subcategory
    else:
        category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        location = request.POST.get('location', 'User Location')
        booking = Booking.objects.create(user=request.user, category=category, user_location=location)
        return redirect('booking_status', booking_id=booking.id)
    context = {'category': category}
    if subcategory_id:
        context['subcategory_id'] = subcategory_id
    return render(request, 'book_service.html', context)

from django.http import Http404

@login_required
def book_service_detail(request, service_type, service_id):
    if service_type == 'category':
        service = get_object_or_404(Category, id=service_id)
    elif service_type == 'subcategory':
        service = get_object_or_404(SubCategory, id=service_id)
    else:
        raise Http404("Service type not found")
    return render(request, 'BOOK.html', {'service': service})

@login_required
def booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_status.html', {'booking': booking})

@login_required
def worker_dashboard(request):
    if not hasattr(request.user, 'workerprofile'):
        return redirect('home')
    pending_bookings = Booking.objects.filter(category__in=request.user.workerprofile.categories.all(), status='pending')
    accepted_bookings = Booking.objects.filter(worker=request.user.workerprofile, status='accepted').order_by('-id')
    return render(request, 'worker_dashboard.html', {
        'pending_bookings': pending_bookings,
        'accepted_bookings': accepted_bookings
    })

@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if hasattr(request.user, 'workerprofile') and booking.status == 'pending':
        from django.db import transaction
        with transaction.atomic():
            booking = Booking.objects.select_for_update().get(id=booking_id)
            if booking.status == 'pending':
                booking.worker = request.user.workerprofile
                booking.status = 'accepted'
                booking.save()
    # print(f"Booking accepted: {booking.id}")  # Debugging line

    return redirect('chat', booking_id=booking.id)  # Updated redirect


@login_required
def decline_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if hasattr(request.user, 'workerprofile') and booking.status == 'pending':
        booking.status = 'declined'
        booking.save()
    return redirect('worker_dashboard')

@login_required
def chat(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user == booking.user or (booking.worker and request.user == booking.worker.user):
        if request.method == 'POST':
            content = request.POST.get('content')
            if content:
                Message.objects.create(booking=booking, sender=request.user, content=content)
            return redirect('chat', booking_id=booking.id)
        messages = booking.message_set.all()
        return render(request, 'chat.html', {'booking': booking, 'messages': messages})
    return redirect('home')

@require_GET
@login_required
def check_new_bookings(request):
    if not hasattr(request.user, 'workerprofile'):
        return JsonResponse({'status': 'error', 'message': 'Not a worker'}, status=403)
    pending_bookings = Booking.objects.filter(
        category__in=request.user.workerprofile.categories.all(),
        status='pending'
    ).values('id', 'category__name', 'user__username', 'user_location')
    return JsonResponse({'status': 'success', 'bookings': list(pending_bookings)})
