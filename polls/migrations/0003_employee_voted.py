# Generated by Django 3.0.3 on 2020-03-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200330_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]
