# Generated by Django 3.0.7 on 2021-05-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('desig', models.CharField(max_length=20)),
            ],
        ),
    ]