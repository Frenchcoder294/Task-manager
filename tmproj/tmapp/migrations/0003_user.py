# Generated by Django 4.2.2 on 2023-06-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmapp', '0002_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
