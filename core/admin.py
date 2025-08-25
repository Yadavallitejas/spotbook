from django.contrib import admin
from .models import Category, WorkerProfile, Booking, Message, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price_range', 'included_services')
    fields = ('name', 'category_image', 'description', 'price_range', 'included_services')

admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkerProfile)
admin.site.register(Booking)
admin.site.register(Message)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_name')

    def category_name(self, obj):
        return obj.category.name

admin.site.register(SubCategory, SubCategoryAdmin)
