# Generated by Django 4.0.3 on 2022-04-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]