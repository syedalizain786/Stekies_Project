# Generated by Django 5.1 on 2024-08-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(max_length=200)),
                ('max_price', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('no_of_rooms', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
