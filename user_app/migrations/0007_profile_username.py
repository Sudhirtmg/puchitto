# Generated by Django 5.0.1 on 2024-01-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_profile_delete_profileview'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
