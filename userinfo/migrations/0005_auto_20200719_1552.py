# Generated by Django 3.0.8 on 2020-07-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_auto_20200719_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
