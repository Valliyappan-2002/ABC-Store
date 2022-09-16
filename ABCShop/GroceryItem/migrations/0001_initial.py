# Generated by Django 3.2.9 on 2022-01-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('typ', models.CharField(choices=[['oil', 'Oil'], ['grain', 'Grain'], ['cosmetic', 'Cosmetic']], max_length=30)),
                ('quantity', models.CharField(max_length=3)),
                ('rpu', models.CharField(max_length=5)),
                ('amount', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
