# Generated by Django 3.1 on 2021-02-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0020_auto_20210210_0941"),
    ]

    operations = [
        migrations.AddField(
            model_name="answergroup",
            name="prefix",
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Prefix"),
        ),
        migrations.AddField(
            model_name="answergroup",
            name="suffix",
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Suffix"),
        ),
    ]