# Generated by Django 3.0.8 on 2020-08-02 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentg', '0008_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['date_time'], 'verbose_name_plural': 'Replies'},
        ),
    ]