# Generated by Django 4.0.4 on 2022-05-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='payment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
