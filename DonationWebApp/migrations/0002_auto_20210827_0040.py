# Generated by Django 3.2 on 2021-08-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DonationWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminloginmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='requestfordonation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userinfomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
