# Generated by Django 4.0.5 on 2022-06-30 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='order_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='buyer',
        ),
        migrations.AddField(
            model_name='order',
            name='postalcode',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Varification Pending'), (2, 'DARIFIED'), (3, 'Delivered')], default=1, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town',
            field=models.CharField(default='', max_length=56),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=21),
        ),
    ]