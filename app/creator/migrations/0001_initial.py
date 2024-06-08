# Generated by Django 5.0.6 on 2024-06-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=240, verbose_name='Message')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Clip',
            },
        ),
    ]
