# Generated by Django 4.1.7 on 2023-05-02 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
    ]