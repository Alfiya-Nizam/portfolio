# Generated by Django 4.0.4 on 2024-04-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('education', models.CharField(max_length=100)),
                ('work_experience', models.TextField()),
                ('certifications', models.TextField()),
                ('accomplishments', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
