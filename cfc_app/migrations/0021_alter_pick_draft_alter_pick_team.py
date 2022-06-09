# Generated by Django 4.0.5 on 2022-06-08 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0020_remove_draft_player_draft_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='draft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cfc_app.draft'),
        ),
        migrations.AlterField(
            model_name='pick',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cfc_app.fbsteam'),
        ),
    ]