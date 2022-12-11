from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from .models import Project
from accounts.models import Engineer


class ProjectImageUploadTest(TestCase):

    def setUp(self):
        self.engineer = Engineer.objects.create(username='Engineer')
        self.project = {
                'engineer': self.engineer,
                'name': 'Test project',
                'tech_used': 'Test tech',
                'updated': timezone.now(),
                'created': timezone.now(),
                'image': None,
                'description': 'Test description',
                'repo_url': 'https://github.com/TimOsahenru/dev-locate',
                'live_url': 'http://timosahenru.pythonanywhere.com/',
                'make_public': False
            }
        self.obj = Project.objects.create(**self.project)

    def test_upload_image(self):

        self.assertEquals(self.obj.image_url, '')
