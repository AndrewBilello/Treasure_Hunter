# Generated by Django 2.2 on 2021-09-09 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Treasures', '0002_auto_20210909_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_created', to='Accounts.User')),
                ('treasure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_posts', to='Treasures.Treasure')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_created', to='Accounts.User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_comments', to='Treasures.Post')),
            ],
        ),
    ]