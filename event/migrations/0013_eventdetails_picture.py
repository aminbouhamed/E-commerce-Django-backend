# Generated by Django 4.2.1 on 2023-08-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_remove_eventdetails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
