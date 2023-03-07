# Generated by Django 4.1.3 on 2023-03-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Designation',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='office_id',
            field=models.PositiveIntegerField(blank=True, max_length=4, null=True),
        ),
    ]