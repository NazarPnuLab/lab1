from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import (
    ContactInfo,
    ContactForm,
    GalleryPhoto,
    EmailReciplents
)

from .serializers import (
    ContactInfoSerializer,
    GalleryPhotoSerializer
)

from .mail import send_email

# Create your views here.
class ContactInfoView(APIView):
    @extend_schema(
        summary="Get contact info",
        description="Get contact info",
        responses={
            200: ContactInfoSerializer,
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def get(self, request):
        try:
            contact_info = ContactInfo.objects.first()
            serializer = ContactInfoSerializer(contact_info)
            return Response(serializer.data)
        except ContactInfo.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'error': 'Contact info not found'}
            )


@csrf_exempt
def contact_form_view(request):
    """Contact form view - completely CSRF exempt"""
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            
            # Create contact form
            contact_form = ContactForm.objects.create(
                name=data.get('name'),
                phone=data.get('phone'),
                email=data.get('email')
            )
            
            # Send email
            send_email(
                subject="New contact form",
                message=f"New contact form: \n\
                    Name: {contact_form.name}\n\
                    Phone: {contact_form.phone}\n\
                    Email: {contact_form.email}",
                recipients=EmailReciplents.objects.all().values_list('email', flat=True)
            )
            
            return JsonResponse({
                'id': contact_form.id,
                'name': contact_form.name,
                'phone': contact_form.phone,
                'email': contact_form.email
            })
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=400
            )
    return JsonResponse({'error': 'Method not allowed'}, status=405)
        

class GalleryPhotoView(APIView):
    @extend_schema(
        summary="Get gallery photos",
        description="Get active gallery photos",
        responses={
            200: GalleryPhotoSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def get(self, request):
        try:
            gallery_photos = GalleryPhoto.objects.filter(is_active=True)
            serializer = GalleryPhotoSerializer(gallery_photos, many=True)
            return Response(serializer.data)
        except GalleryPhoto.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'error': 'Gallery photos not found'}
            )


# TEST
# TEST