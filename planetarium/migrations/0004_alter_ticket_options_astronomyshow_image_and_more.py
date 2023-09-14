# Generated by Django 4.2.4 on 2023-08-10 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import planetarium.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("planetarium", "0003_planetariumdome_seats_in_row"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ticket",
            options={"ordering": ["row", "seat"]},
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="image",
            field=models.ImageField(
                null=True, upload_to=planetarium.models.astronomy_show_image_file_path
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("show_session", "row", "seat")},
        ),
    ]
