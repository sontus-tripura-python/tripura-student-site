# Generated by Django 2.2.6 on 2019-11-12 03:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_profile_current_work'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]