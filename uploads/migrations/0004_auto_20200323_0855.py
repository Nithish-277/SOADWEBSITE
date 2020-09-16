# Generated by Django 3.0.2 on 2020-03-23 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0003_upload_prescription_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_prescription',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]