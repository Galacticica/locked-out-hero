# Generated by Django 5.1.6 on 2025-02-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='j_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
