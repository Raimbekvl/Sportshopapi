# Generated by Django 3.2 on 2022-08-25 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='user',
        ),
    ]
