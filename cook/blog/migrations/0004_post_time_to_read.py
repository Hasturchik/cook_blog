# Generated by Django 4.2.5 on 2023-10-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_directions_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_to_read',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
