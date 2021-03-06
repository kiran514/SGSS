# Generated by Django 3.0.2 on 2020-06-07 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('redressal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('daytoken', models.IntegerField()),
                ('last_update', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=10)),
                ('message', models.TextField(max_length=1000)),
                ('subject', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(choices=[('University', 'University'), ('Institute', 'Institute'), ('Department', 'Department')], max_length=15)),
                ('redressal_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', to='redressal.RedressalBody')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.SubCategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'daytoken')},
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=1000)),
                ('grievance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='studentg.Grievance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
