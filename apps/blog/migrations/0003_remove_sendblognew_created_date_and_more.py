# Generated by Django 5.0.2 on 2024-02-22 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_contentnewblog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendblognew',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='sendblognew',
            name='modified_date',
        ),
    ]
