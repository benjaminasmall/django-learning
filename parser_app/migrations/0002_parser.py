# Generated by Django 4.2.7 on 2023-11-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mpanCore", models.CharField(max_length=13)),
                ("serialNo", models.CharField(max_length=10)),
                ("unique_serial", models.IntegerField()),
                ("ReadingDt", models.DateTimeField()),
                ("readingVal", models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
    ]