# Generated by Django 3.1.7 on 2021-03-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='mobile',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='pf_number',
            field=models.TextField(default='', unique=True),
        ),
    ]
