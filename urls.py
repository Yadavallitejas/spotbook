from django.urls import path, re_path
from core.views import create_subcategory, subcategory_list, get_workers_for_category 

from django.conf import settings  # Import settings for media files
from django.views.static import serve  # Import serve for serving media files
from core.views import home, user_signup, worker_signup, user_login, user_logout, book_service, booking_status, worker_dashboard, accept_booking, decline_booking, chat, check_new_bookings, services , book_service_detail, contact, privacy, terms # Added chat import

urlpatterns = [ 
    path('create-subcategory/', create_subcategory, name='create_subcategory'),
    path('subcategories/', subcategory_list, name='subcategory_list'),
    path('workers/<int:category_id>/', get_workers_for_category, name='get_workers_for_category'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Serve media files
    path('', home, name='home'),
    path('signup/user/', user_signup, name='user_signup'),
    path('signup/worker/', worker_signup, name='worker_signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),  # Added logout URL pattern
    path('book_service/<int:category_id>/', book_service, name='book_service'),  # Added book service URL pattern
    path('book_service/<int:category_id>/<int:subcategory_id>/', book_service, name='book_service_with_subcategory'),  # New URL pattern with subcategory
    path('book_service_detail/<str:service_type>/<int:service_id>/', book_service_detail, name='book_service_detail'),  # Updated URL pattern for category or subcategory
    path('booking_status/<int:booking_id>/', booking_status, name='booking_status'),  # Added booking status URL pattern
    path('worker_dashboard/', worker_dashboard, name='worker_dashboard'),  # Added worker dashboard URL pattern
    path('accept/<int:booking_id>/', accept_booking, name='accept_booking'),  # Added accept booking URL pattern
    path('decline_booking/<int:booking_id>/', decline_booking, name='decline_booking'),  # Added decline booking URL pattern
    path('chat/<int:booking_id>/', chat, name='chat'),  # Added chat URL pattern
    path('check-new-bookings/', check_new_bookings, name='check_new_bookings'),
    path('services', services, name='services'),  # Added services URL pattern
    path('contact', contact, name='contact'),  # Added contact URL pattern
    path('privacy', privacy, name='privacy'),  # Added privacy URL pattern
    path('terms', terms, name='terms'),  # Added terms URL pattern
]
