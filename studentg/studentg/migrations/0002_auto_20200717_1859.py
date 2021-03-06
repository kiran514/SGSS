# Generated by Django 3.0.8 on 2020-07-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='category_new',
            field=models.PositiveSmallIntegerField(choices=[(1, 'University'), (2, 'Institute'), (3, 'Department')], null=True),
        ),
        migrations.AddField(
            model_name='grievance',
            name='status_new',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Draft'), (2, 'In Review'), (3, 'Pending'), (4, 'Resolved'), (5, 'Rejected')], null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
    ]
