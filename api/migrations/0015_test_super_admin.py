# Generated by Django 2.1.4 on 2019-01-10 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190110_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='super_admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.SuperAdmin'),
            preserve_default=False,
        ),
    ]
