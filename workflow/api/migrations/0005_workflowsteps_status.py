# Generated by Django 3.0.5 on 2020-04-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200422_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowsteps',
            name='status',
            field=models.IntegerField(choices=[(0, 'In definition'), (1, 'Active'), (2, 'Retired')], default=0, verbose_name='Status'),
        ),
    ]
