# Generated by Django 3.1.5 on 2021-01-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='big_room_mark',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='common_room_mark',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='small_room_mark',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
