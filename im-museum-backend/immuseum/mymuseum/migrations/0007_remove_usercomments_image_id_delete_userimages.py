# Generated by Django 4.1.13 on 2024-02-29 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymuseum', '0006_alter_userdetails_subscribed_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomments',
            name='image_id',
        ),
        migrations.DeleteModel(
            name='UserImages',
        ),
    ]