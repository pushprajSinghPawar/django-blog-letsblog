# Generated by Django 4.0.1 on 2022-04-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blogpost_blogpost_category1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='Blogpost_blog',
            field=models.TextField(max_length=400),
        ),
    ]
