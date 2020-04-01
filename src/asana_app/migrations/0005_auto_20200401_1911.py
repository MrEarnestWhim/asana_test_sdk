# Generated by Django 2.2.12 on 2020-04-01 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asana_app', '0004_auto_20200401_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AddField(
            model_name='sections',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='asana_app.Project'),
            preserve_default=False,
        ),
    ]
