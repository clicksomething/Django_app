# Generated by Django 4.2.7 on 2023-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_employee_session_stranger_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
