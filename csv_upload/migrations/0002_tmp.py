# Generated by Django 3.0.7 on 2020-06-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmp', models.CharField(max_length=100)),
            ],
        ),
    ]
