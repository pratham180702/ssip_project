# Generated by Django 3.0.5 on 2022-10-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminusers',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
