# Generated by Django 2.2.4 on 2020-04-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_item_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='USAorder',
            fields=[
                ('userid', models.TextField(primary_key=True, serialize=False)),
                ('total_cost', models.TextField()),
                ('discription', models.TextField()),
            ],
        ),
    ]
