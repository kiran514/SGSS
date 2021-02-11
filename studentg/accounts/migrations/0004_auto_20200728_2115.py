# Generated by Django 3.0.8 on 2020-07-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200717_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('ADM', 'Admin'), ('STU', 'Student'), ('UNI', 'University Member'), ('INS', 'Institute Member'), ('DEP', 'Department Member'), ('UNI_H', 'University Head'), ('INS_H', 'Institute Head'), ('DEP_H', 'Department Head')], max_length=5),
        ),
    ]