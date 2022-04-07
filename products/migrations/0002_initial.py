# Generated by Django 4.0.3 on 2022-04-06 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('user_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodotti',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prodotti', to='user_manage.owner'),
        ),
    ]
