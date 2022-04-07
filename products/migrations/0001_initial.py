# Generated by Django 4.0.3 on 2022-04-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=255)),
                ('review', models.TextField(default='Hello')),
                ('image', models.ImageField(blank=True, upload_to='img/')),
            ],
        ),
    ]
