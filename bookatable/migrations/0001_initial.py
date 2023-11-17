# Generated by Django 4.2.7 on 2023-11-17 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('10:00', '10:00 - 10:45'), ('11:00', '11:00 - 11:45'), ('12:00', '12:00 - 12:45'), ('13:00', '13:00 - 13:45'), ('14:00', '14:00 - 14:45'), ('15:00', '15:00 - 15:45'), ('16:00', '16:00 - 16:45'), ('17:00', '17:00 - 17:45'), ('18:00', '18:00 - 18:45'), ('19:00', '19:00 - 19:45'), ('20:00', '20:00 - 20:45'), ('21:00', '21:00 - 21:45'), ('22:00', '22:00 - 22:45')], default='10:00 - 10:45', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('people', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '4'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
