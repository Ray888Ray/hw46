# Generated by Django 4.1.3 on 2022-11-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_todo_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Description'),
        ),
    ]
