# Generated by Django 2.0.7 on 2018-08-02 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='super_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SuperAdmin'),
        ),
    ]
