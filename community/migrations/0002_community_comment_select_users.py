# Generated by Django 3.0.7 on 2020-07-04 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='comment_select_users',
            field=models.ManyToManyField(blank=True, related_name='comment_select_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
