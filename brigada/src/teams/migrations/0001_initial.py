# Generated by Django 4.1.5 on 2023-01-07 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=100, verbose_name="Бригада")),
                ("amount_people", models.IntegerField(verbose_name="Количество людей")),
                (
                    "head",
                    models.CharField(max_length=200, verbose_name="ФИО ответственного"),
                ),
                (
                    "qualification",
                    models.CharField(
                        max_length=150, verbose_name="Должность ответственного"
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cities.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Бригада",
                "verbose_name_plural": "Бригады",
                "ordering": ["name", "city"],
            },
        ),
    ]
