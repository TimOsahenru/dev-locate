from django.test import TestCase
from .models import Project
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO


class TestModels(TestCase):
    def setUp(self):
        new_image = BytesIO()
        self.image = Project.objects.create(
            image=ImageFile(new_image)
        )

    def test_image_url(self):

        self.assertEquals(self.image.image_url, '')
