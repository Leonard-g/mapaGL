# Generated by Django 4.1.7 on 2023-03-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_remove_task_datecompleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="datecompleted",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="Medidor",
            field=models.IntegerField(),
        ),
    ]