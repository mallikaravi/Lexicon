# Generated by Django 2.2.28 on 2022-06-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=10)),
                ('course', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
            ],
        ),
    ]
