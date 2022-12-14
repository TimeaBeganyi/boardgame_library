# Generated by Django 4.1 on 2022-10-12 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userextend', '0002_userprofile'),
        ('boardgames', '0013_alter_boardgamecomment_rating_boardgameinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='favourite',
            field=models.ManyToManyField(related_name='user_fav', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='boardgamecomment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userextend.userextend'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boardgames.boardgame'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userextend.userextend'),
        ),
    ]
