# Generated by Django 5.1 on 2024-09-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('radiation_level', models.FloatField(db_index=True, help_text='em µSv/h')),
                ('altitude', models.FloatField(db_index=True, help_text='em m')),
            ],
        ),
        migrations.AlterField(
            model_name='radioactivematerial',
            name='constant',
            field=models.FloatField(db_index=True, help_text='em µSv.m2/h.GBq'),
        ),
    ]
