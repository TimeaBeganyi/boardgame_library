# Generated by Django 4.1 on 2022-09-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0009_boardgamecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardgame',
            options={'ordering': ['-title']},
        ),
        migrations.AddField(
            model_name='boardgamecomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
