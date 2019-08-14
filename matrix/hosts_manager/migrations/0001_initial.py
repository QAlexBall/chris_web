# Generated by Django 2.2 on 2019-07-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=20)),
                ('host_ip', models.CharField(max_length=20)),
                ('port', models.IntegerField()),
                ('default_path', models.CharField(max_length=200)),
            ],
        ),
    ]
