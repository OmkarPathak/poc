# Generated by Django 2.1.7 on 2019-03-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrendTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_one', models.IntegerField()),
                ('slider_two', models.IntegerField()),
                ('slider_three', models.IntegerField()),
                ('slider_four', models.IntegerField()),
                ('slider_five', models.IntegerField()),
                ('lowest_value', models.IntegerField()),
                ('highest_value', models.IntegerField()),
                ('mean_value', models.FloatField()),
            ],
        ),
    ]
