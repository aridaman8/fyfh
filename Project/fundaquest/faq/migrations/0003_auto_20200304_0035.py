# Generated by Django 3.0.1 on 2020-03-03 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20200303_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='qid',
            new_name='question',
        ),
    ]