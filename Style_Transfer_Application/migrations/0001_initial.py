# Generated by Django 3.0.3 on 2020-08-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_content', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img_style', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]