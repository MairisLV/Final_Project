# Generated by Django 3.2.2 on 2021-05-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='interest_pmt',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='loans',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
