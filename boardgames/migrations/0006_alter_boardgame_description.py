# Generated by Django 4.1 on 2022-09-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0005_alter_boardgame_categories_alter_boardgame_mechanics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='description',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]