# Generated by Django 4.1.3 on 2023-03-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_designation_userprofile_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='office_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
