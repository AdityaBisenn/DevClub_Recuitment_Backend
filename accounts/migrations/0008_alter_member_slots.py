# Generated by Django 4.1 on 2022-08-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_slot_capacity_court_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slots',
            field=models.ManyToManyField(blank=True, to='accounts.slot'),
        ),
    ]
