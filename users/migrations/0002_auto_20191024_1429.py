# Generated by Django 2.2.6 on 2019-10-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='I love awwwards,it is a source of inspiration', max_length=250),
        ),
    ]
