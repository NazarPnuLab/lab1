from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Phone",
        null=True,
        blank=True
    )
    facebook = models.URLField(
        max_length=255,
        verbose_name="Facebook URL",
        null=True,
        blank=True
    )
    whatsapp = models.URLField(
        max_length=255,
        verbose_name="Whatsapp URL",
        null=True,
        blank=True
    )
    cart_link = models.URLField(
        max_length=512,
        verbose_name="Cart Link",
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Address",
        null=True,
        blank=True
    )
    reviews_link = models.URLField(
        max_length=255,
        verbose_name="Reviews Link",
        null=True,
        blank=True
    )


    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email or ""


class ContactForm(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Name",
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Last Name",
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Address",
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Phone",
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        null=True,
        blank=True
    )
    message = models.CharField(
        max_length=255,
        verbose_name="Message",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Form"

    def __str__(self):
        return f"{self.first_name or ''} - {self.phone or ''} - {self.email or ''}"
    

class GalleryPhoto(models.Model):
    photo = models.ImageField(
        upload_to='gallery/',
        verbose_name="Photo",
        null=True,
        blank=True
    )
    meta_title = models.CharField(
        max_length=255,
        verbose_name="Meta Title",
        null=True,
        blank=True
    )
    meta_description = models.CharField(
        max_length=255,
        verbose_name="Meta Description",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    alt = models.CharField(
        max_length=255,
        verbose_name="Alt",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active"
    )

    class Meta:
        verbose_name = "Gallery Photo"
        verbose_name_plural = "Gallery Photo"

    def __str__(self):
        return self.photo.name if self.photo else ""


class EmailReciplents(models.Model):
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
    )

    class Meta:
        verbose_name = "Email Recipient"
        verbose_name_plural = "Email Recipients"

    def __str__(self):
        return self.email
