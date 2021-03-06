# Generated by Django 3.0.6 on 2020-05-13 19:35

from django.db import migrations, models
import subapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Job', 'JOB'), ('Internship', 'INTERNSHIP')], max_length=128)),
                ('Description', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('official_link', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=subapp.models.new_file_name)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stream', models.CharField(choices=[('B', 'BTECH'), ('M', 'MTECH')], max_length=128)),
            ],
        ),
    ]
