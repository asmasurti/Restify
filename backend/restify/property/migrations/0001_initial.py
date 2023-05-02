# Generated by Django 4.1.7 on 2023-03-25 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('num_bedrooms', models.PositiveIntegerField()),
                ('num_bathrooms', models.PositiveIntegerField()),
                ('num_guests', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=property.models.user_directory_path)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(choices=[('Pool', 'Pool'), ('Wi-Fi', 'Wi-Fi'), ('Air Conditioning', 'Air Conditioning'), ('Heating', 'Heating'), ('Pets Allowed', 'Pets Allowed'), ('Washer and Dryer', 'Washer and Dryer'), ('Jacuzzi', 'Jacuzzi'), ('Free Parking', 'Free Parking'), ('Equipped Kitchen', 'Equipped Kitchen'), ('Fireplace', 'Fireplace')], max_length=30)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='property.property')),
            ],
            options={
                'unique_together': {('amenity', 'property')},
            },
        ),
    ]
