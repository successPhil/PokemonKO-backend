# Generated by Django 4.2.5 on 2023-10-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_alter_pokemon_defense_alter_pokemon_health_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(default=420),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='max_health',
            field=models.IntegerField(default=420),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='power',
            field=models.IntegerField(default=115),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='totalXP',
            field=models.IntegerField(default=1125),
        ),
    ]
