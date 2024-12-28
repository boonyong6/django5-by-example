# Generated by Django 5.1.4 on 2024-12-28 04:08

from django.apps.registry import Apps
from django.db import migrations

from ..models import Image


def patch_image_total_likes(apps: Apps, schema_editor):
    image_model: Image = apps.get_model("images", "Image")
    for image in image_model.objects.all():
        image.total_likes = image.users_like.count()
        image.save()


def undo_patch_image_total_likes(apps: Apps, schema_editor):
    image_model: Image = apps.get_model("images", "Image")
    image_model.objects.update(total_likes=0)


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_image_total_likes_and_more"),
    ]

    operations = [
        migrations.RunPython(patch_image_total_likes, undo_patch_image_total_likes),
    ]
