# Generated by Django 3.0.6 on 2020-06-03 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=200)),
                ('tz', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Activity_periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='start_time')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.User')),
            ],
        ),
    ]