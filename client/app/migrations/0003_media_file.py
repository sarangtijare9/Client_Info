# Generated by Django 2.2.7 on 2020-10-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201028_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=50)),
            ],
        ),
    ]
