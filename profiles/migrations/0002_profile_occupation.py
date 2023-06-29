# Generated by Django 3.2.19 on 2023-06-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(choices=[('food_enthusiast', 'Food Enthusiast'), ('chef', 'Chef'), ('bartender', 'Bartender'), ('barista', 'Barista'), ('home_cook', 'Home Cook')], default='food_enthusiast', max_length=255),
        ),
    ]
