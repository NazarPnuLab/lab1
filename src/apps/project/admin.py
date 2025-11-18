from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    ContactInfo,
    ContactForm,
    GalleryPhoto,
    EmailReciplents
)

admin.site.unregister(Group)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'facebook', 'whatsapp']
    list_filter = ['email']
    search_fields = ['email', 'phone']
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(ContactInfo, ContactInfoAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'phone', 'email']
    search_fields = ['first_name', 'last_name', 'address', 'phone', 'email']
    ordering = ['-id']
    
    def has_add_permission(self, request):
        return False

admin.site.register(ContactForm, ContactFormAdmin)


class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'alt', 'meta_title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['alt', 'meta_title', 'meta_description']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Main information', {
            'fields': ('photo', 'alt', 'is_active')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('System information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(GalleryPhoto, GalleryPhotoAdmin)

admin.site.register(EmailReciplents)


