from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)  # e.g., Plumbing, Electrician
    category_image = models.ImageField(upload_to='category_images/', blank=True)
    description = models.TextField(blank=True)
    price_range = models.CharField(max_length=100, blank=True)
    included_services = models.TextField(blank=True)

    def __str__(self):
        return self.name  # Return the name of the category


class SubCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., Plumbing Repair
    description = models.TextField()  # Description of the subcategory
    expected_price_range = models.CharField(max_length=100)  # e.g., $50 - $100
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    subcategory_image = models.ImageField(upload_to='subcategory_images/', blank=True)  # New field for subcategory image


    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.categories}"

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ], default='pending')
    user_location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.status}"

class Message(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} - {self.timestamp}"
