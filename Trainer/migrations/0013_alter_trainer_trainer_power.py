# Generated by Django 4.2.5 on 2023-10-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0012_trainer_enemy_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='trainer_power',
            field=models.IntegerField(default=3),
        ),
    ]
