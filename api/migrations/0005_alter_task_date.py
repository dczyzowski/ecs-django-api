# Generated by Django 4.1.3 on 2022-11-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_task_user_alter_task_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default='30-11-2022', null=True),
        ),
    ]