# Generated by Django 4.0.3 on 2022-04-16 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timeline', '0004_comment_published_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]