# Generated by Django 5.1.3 on 2024-12-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0017_course_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='UserModuleCompletion',
        ),
    ]