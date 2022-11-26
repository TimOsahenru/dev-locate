# Generated by Django 4.1.2 on 2022-11-23 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Max 100 char", max_length=100)),
                (
                    "tech_used",
                    models.CharField(default="stack_one | stack_two", max_length=200),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("make_public", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True, null=True)),
                ("repo_url", models.URLField(blank=True, null=True)),
                ("live_url", models.URLField(blank=True, null=True)),
                (
                    "engineer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
            },
        ),
    ]