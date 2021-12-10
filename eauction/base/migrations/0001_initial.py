# Generated by Django 4.0 on 2021-12-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='')),
                ('minimum_bid_price', models.CharField(max_length=20)),
                ('auction_end_time', models.DateTimeField()),
            ],
        ),
    ]
