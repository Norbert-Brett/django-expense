# Generated by Django 4.2.1 on 2023-05-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('utilities', 'Utilities'), ('rent', 'Rent'), ('transportation', 'Transportation'), ('other', 'Other')], max_length=50),
        ),
    ]
