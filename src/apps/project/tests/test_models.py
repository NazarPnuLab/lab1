import pytest

from apps.project.models import (
    ContactInfo,
    ContactForm,
    GalleryPhoto,
    EmailReciplents,
)


@pytest.mark.django_db
class TestContactInfo:
    def test_str_with_email(self):
        contact = ContactInfo.objects.create(email="test@example.com")
        assert str(contact) == "test@example.com"

    def test_str_without_email(self):
        contact = ContactInfo.objects.create(email=None)
        assert str(contact) == ""

    def test_all_fields_optional(self):
        contact = ContactInfo.objects.create()
        assert contact.email is None
        assert contact.phone is None
        assert contact.facebook is None
        assert contact.whatsapp is None
        assert contact.cart_link is None
        assert contact.address is None
        assert contact.reviews_link is None

    def test_create_with_all_fields(self):
        contact = ContactInfo.objects.create(
            email="test@example.com",
            phone="+1234567890",
            facebook="https://facebook.com/test",
            whatsapp="https://wa.me/1234567890",
            cart_link="https://example.com/cart",
            address="123 Main St",
            reviews_link="https://example.com/reviews"
        )
        assert contact.email == "test@example.com"
        assert contact.phone == "+1234567890"
        assert contact.facebook == "https://facebook.com/test"


@pytest.mark.django_db
class TestContactForm:
    def test_str_contains_all_fields(self):
        form = ContactForm.objects.create(
            first_name="John",
            phone="123456789",
            email="john@example.com",
        )
        s = str(form)
        assert "John" in s
        assert "123456789" in s
        assert "john@example.com" in s

    def test_str_with_none_values(self):
        form = ContactForm.objects.create(
            first_name=None,
            phone=None,
            email=None,
        )
        s = str(form)
        assert s == " -  - "  # Empty strings separated by dashes

    def test_all_fields_optional(self):
        form = ContactForm.objects.create()
        assert form.first_name is None
        assert form.last_name is None
        assert form.address is None
        assert form.phone is None
        assert form.email is None
        assert form.message is None

    def test_create_with_all_fields(self):
        form = ContactForm.objects.create(
            first_name="John",
            last_name="Doe",
            address="123 Main St",
            phone="+1234567890",
            email="john@example.com",
            message="Hello world"
        )
        assert form.first_name == "John"
        assert form.last_name == "Doe"
        assert form.message == "Hello world"


@pytest.mark.django_db
class TestGalleryPhoto:
    def test_defaults(self):
        photo = GalleryPhoto.objects.create()
        assert photo.is_active is True
        assert photo.created_at is not None
        # ImageField returns ImageFieldFile object, check if it's empty
        assert not photo.photo or not photo.photo.name

    def test_str_without_photo(self):
        photo = GalleryPhoto.objects.create(meta_title="Test")
        # __str__ returns empty string if no photo file
        result = str(photo)
        assert result == ""

    def test_all_optional_fields(self):
        photo = GalleryPhoto.objects.create()
        # ImageField returns ImageFieldFile object, check if it's empty
        assert not photo.photo or not photo.photo.name
        assert photo.meta_title is None
        assert photo.meta_description is None
        assert photo.alt is None

    def test_create_with_all_fields(self):
        photo = GalleryPhoto.objects.create(
            meta_title="Test Title",
            meta_description="Test Description",
            alt="Test Alt",
            is_active=False
        )
        assert photo.meta_title == "Test Title"
        assert photo.meta_description == "Test Description"
        assert photo.alt == "Test Alt"
        assert photo.is_active is False
        assert photo.created_at is not None


@pytest.mark.django_db
class TestEmailReciplents:
    def test_str_returns_email(self):
        item = EmailReciplents.objects.create(email="rcpt@example.com")
        assert str(item) == "rcpt@example.com"

    def test_email_required(self):
        with pytest.raises(Exception):  # IntegrityError or ValidationError
            EmailReciplents.objects.create(email=None)

    def test_create_with_valid_email(self):
        item = EmailReciplents.objects.create(email="test@example.com")
        assert item.email == "test@example.com"
        assert str(item) == "test@example.com"


