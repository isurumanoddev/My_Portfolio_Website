# Generated by Django 4.1.7 on 2023-03-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0007_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]