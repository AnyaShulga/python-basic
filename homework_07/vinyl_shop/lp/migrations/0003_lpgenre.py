# Generated by Django 4.1.3 on 2022-11-09 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0002_lp_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='LpGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('lp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lp.lp')),
            ],
        ),
    ]
