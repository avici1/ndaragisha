# Generated by Django 2.2.2 on 2019-07-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190723_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundbutnotassigned',
            name='owner_email',
            field=models.CharField(default='empty', max_length=30),
        ),
        migrations.AddField(
            model_name='lostitems',
            name='owner_email',
            field=models.CharField(default='empty', max_length=40),
        ),
    ]
