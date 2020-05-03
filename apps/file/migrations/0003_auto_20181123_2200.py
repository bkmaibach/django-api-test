# Generated by Django 2.1.2 on 2018-11-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_file_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='is_resized',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='mime_type',
            field=models.CharField(db_index=True, default='application/octet-stream', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
