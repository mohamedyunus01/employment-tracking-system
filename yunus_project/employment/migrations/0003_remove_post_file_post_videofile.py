# Generated by Django 4.2.1 on 2023-07-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
