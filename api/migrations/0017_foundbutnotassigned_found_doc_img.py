# Generated by Django 2.2.2 on 2019-07-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_foundbutnotassigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundbutnotassigned',
            name='found_doc_img',
            field=models.CharField(default='empty', max_length=120),
        ),
    ]
