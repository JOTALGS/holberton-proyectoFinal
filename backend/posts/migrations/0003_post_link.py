# Generated by Django 4.2.13 on 2024-06-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
