# Generated by Django 2.1.4 on 2019-01-31 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190131_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestresult',
            name='testAttemptDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]