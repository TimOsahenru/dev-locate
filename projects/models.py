from django.db import models
from accounts.models import Engineer


class Project(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Max 100 char')
    tech_used = models.CharField(max_length=200, default='stack_one | stack_two')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='project.png')
    description = models.TextField(null=True, blank=True)
    repo_url = models.URLField(null=True, blank=True)
    live_url = models. URLField(null=True, blank=True)
    make_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ['-created']
