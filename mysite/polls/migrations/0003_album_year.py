# Generated by Django 5.0.6 on 2024-07-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_musician_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]