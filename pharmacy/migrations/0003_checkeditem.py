# Generated by Django 3.2.3 on 2021-05-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_alter_item_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('code', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]