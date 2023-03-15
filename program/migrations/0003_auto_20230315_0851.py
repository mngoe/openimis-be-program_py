# Generated by Django 3.2.17 on 2023-03-15 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_program_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='validityDate',
        ),
        migrations.AddField(
            model_name='program',
            name='validityDateFrom',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Program Validity Start Date'),
        ),
        migrations.AddField(
            model_name='program',
            name='validityDateTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Program Validity End Date'),
        ),
    ]