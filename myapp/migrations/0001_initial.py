# Generated by Django 2.2.6 on 2019-11-04 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('university', models.CharField(max_length=100)),
                ('School', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('fathername', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=50)),
                ('deparment', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('Village', models.CharField(max_length=150)),
                ('thana', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('current_city', models.CharField(max_length=100)),
                ('local_city', models.CharField(max_length=100)),
                ('bio_data', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]