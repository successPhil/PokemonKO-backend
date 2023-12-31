# Generated by Django 4.2.5 on 2023-10-07 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('front_image_url', models.URLField()),
                ('back_image_url', models.URLField()),
                ('health', models.IntegerField()),
                ('moves', models.ManyToManyField(blank=True, related_name='pokemon_moves', to='moves.move')),
            ],
        ),
    ]
