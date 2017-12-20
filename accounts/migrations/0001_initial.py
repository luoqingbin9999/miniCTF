# Generated by Django 2.0 on 2017-12-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('teamname', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('job', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=250)),
            ],
        ),
    ]
