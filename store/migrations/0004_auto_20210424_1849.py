# Generated by Django 3.2 on 2021-04-24 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210424_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
