# Generated by Django 4.2.4 on 2023-08-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planetarium", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="planetariumdome",
            name="seats_in_row",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]