# Generated by Django 3.2.9 on 2021-11-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.CharField(default=None, max_length=512),
        ),
    ]
