# Generated by Django 4.2.7 on 2023-12-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_chessboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('person_id', models.BigIntegerField(max_length=200, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=20)),
            ],
        ),
    ]
