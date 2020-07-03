# Generated by Django 3.0.7 on 2020-06-29 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200629_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('price', models.IntegerField(null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=250, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
