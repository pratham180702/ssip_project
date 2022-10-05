# Generated by Django 3.0.5 on 2022-10-05 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('category_select', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Category')),
            ],
        ),
    ]