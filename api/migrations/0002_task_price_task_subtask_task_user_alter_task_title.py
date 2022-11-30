# Generated by Django 4.1.3 on 2022-11-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='task',
            name='subtask',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=48),
        ),
    ]
