# Generated by Django 3.0.7 on 2020-06-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_upload', '0002_tmp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tmp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
