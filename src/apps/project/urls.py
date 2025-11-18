from django.urls import path
from .views import (
    ContactInfoView,
    contact_form_view,
    GalleryPhotoView,
)

urlpatterns = [
    path('contact-info/', ContactInfoView.as_view(), name='contact-info'),
    path('contact-form/', contact_form_view, name='contact-form'),
    path('gallery-photo/', GalleryPhotoView.as_view(), name='gallery-photo')
]