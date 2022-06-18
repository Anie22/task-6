# Generated by Django 4.0.5 on 2022-06-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='X_Hotel',
            fields=[
                ('Room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Amount_paid', models.IntegerField()),
                ('Occupant_Name', models.CharField(max_length=90)),
                ('Occupant_Email', models.EmailField(max_length=254)),
                ('Occupant_Occupation', models.CharField(max_length=90)),
                ('Number_of_night', models.IntegerField()),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Y_Hotel',
            fields=[
                ('Room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Amount_paid', models.IntegerField()),
                ('Occupant_Name', models.CharField(max_length=90)),
                ('Occupant_Email', models.EmailField(max_length=254)),
                ('Occupant_Occupation', models.CharField(max_length=90)),
                ('Number_of_night', models.IntegerField()),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Z_Hotel',
            fields=[
                ('Room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Amount_paid', models.IntegerField()),
                ('Occupant_Name', models.CharField(max_length=90)),
                ('Occupant_Email', models.EmailField(max_length=254)),
                ('Occupant_Occupation', models.CharField(max_length=90)),
                ('Number_of_night', models.IntegerField()),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='person',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='people',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='patience',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Bio',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]