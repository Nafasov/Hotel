# Generated by Django 5.0.2 on 2024-02-22 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_sendblognew_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentnewblog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_children', to='blog.commentnewblog'),
        ),
    ]