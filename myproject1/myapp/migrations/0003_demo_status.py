# Generated by Django 2.0.1 on 2019-10-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='status',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
