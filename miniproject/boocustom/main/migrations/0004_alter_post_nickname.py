# Generated by Django 4.0.4 on 2022-06-03 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_post_image_alter_post_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='닉네임'),
        ),
    ]
