# Generated by Django 4.0.5 on 2022-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_popularclients'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularclients',
            name='ratting',
            field=models.PositiveIntegerField(default=1, verbose_name='Client`s Ratting'),
            preserve_default=False,
        ),
    ]
