# Generated by Django 4.2 on 2023-05-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('poste', models.CharField(max_length=100)),
            ],
        ),
    ]
