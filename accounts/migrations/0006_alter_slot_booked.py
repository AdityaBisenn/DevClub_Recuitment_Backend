# Generated by Django 4.1 on 2022-08-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_slot_members_member_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='booked',
            field=models.IntegerField(default=0),
        ),
    ]