# Generated by Django 4.2.16 on 2024-11-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0002_auto_20211109_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.bus')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.driver')),
            ],
        ),
    ]
