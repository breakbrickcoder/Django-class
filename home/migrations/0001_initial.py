# Generated by Django 3.2.7 on 2021-09-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
