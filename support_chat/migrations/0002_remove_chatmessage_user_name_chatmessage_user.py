# Generated by Django 5.1.4 on 2025-02-22 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='user_name',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.CharField(default='Anonymous', max_length=255),
            preserve_default=False,
        ),
    ]
