# Generated by Django 3.0.3 on 2020-02-25 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_test_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_upload',
            name='name',
            field=models.CharField(default='as', max_length=255),
        ),
    ]
