# Generated by Django 4.1 on 2022-09-20 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0010_alter_boardgame_options_boardgamecomment_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardgame',
            options={'ordering': ['title']},
        ),
    ]