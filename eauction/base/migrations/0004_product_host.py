# Generated by Django 4.0 on 2021-12-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0003_alter_product_minimum_bid_price_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]