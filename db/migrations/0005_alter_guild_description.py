# Generated by Django 4.0.2 on 2022-07-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]