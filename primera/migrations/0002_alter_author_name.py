# Generated by Django 4.2.2 on 2023-06-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("primera", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=150),
        ),
    ]