# Generated by Django 4.1.1 on 2022-09-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PayPlan",
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
                ("price", models.IntegerField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
