# Generated by Django 5.0.4 on 2024-04-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('Active', models.BooleanField(default=False)),
            ],
        ),
    ]
