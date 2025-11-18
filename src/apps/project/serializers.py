from rest_framework import serializers

from .models import (
    ContactInfo,
    ContactForm,
    GalleryPhoto,
)


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactForm
        fields = '__all__'


class GalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = '__all__'
