# Generated by Django 4.2.8 on 2024-10-17 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aritcle',
            new_name='article',
        ),
    ]
