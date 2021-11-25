# Generated by Django 3.2.9 on 2021-11-25 22:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('categories', models.ManyToManyField(to='food.Category')),
                ('foods', models.ManyToManyField(to='food.Food')),
            ],
        ),
    ]