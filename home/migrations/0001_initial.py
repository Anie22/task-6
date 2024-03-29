# Generated by Django 4.0.5 on 2022-06-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('contact', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=220)),
                ('product_price', models.CharField(max_length=220)),
                ('product_category', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(default='', max_length=255)),
                ('patient_blood_pressure', models.CharField(default='', max_length=255)),
                ('patient_sugar_level', models.CharField(default='', max_length=255)),
                ('patient_disabilities', models.CharField(default='', max_length=255)),
                ('patience', models.ManyToManyField(default='', to='home.people')),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(default='', max_length=255)),
                ('hobbies', models.CharField(default='', max_length=255)),
                ('date_of_birth', models.DateField(default='')),
                ('biggest_achievement', models.CharField(default='', max_length=200)),
                ('people', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.people')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number_and_name', models.CharField(default='', max_length=220)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=40)),
                ('person', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='home.people')),
            ],
        ),
    ]
