# Generated by Django 4.0.5 on 2022-06-22 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0002_alter_draft_players'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pick',
            options={'ordering': ['id']},
        ),
    ]
