# Generated by Django 2.2 on 2021-09-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treasures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]