# Generated by Django 4.0.4 on 2024-04-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
