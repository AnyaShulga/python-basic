# Generated by Django 4.1.3 on 2022-11-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lp',
            name='condition',
            field=models.CharField(default='NM', max_length=2),
            preserve_default=False,
        ),
    ]