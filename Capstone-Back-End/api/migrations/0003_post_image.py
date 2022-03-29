# Generated by Django 4.0.3 on 2022-03-29 20:15

import api.models.post
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=api.models.post.upload_to, verbose_name='Image'),
        ),
    ]
