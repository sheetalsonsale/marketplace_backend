# Generated by Django 5.1.5 on 2025-02-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=32)),
            ],
        ),
    ]
