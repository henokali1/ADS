# Generated by Django 2.1.5 on 2020-03-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbads', '0004_auto_20200314_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='attachmentTitle',
        ),
    ]
