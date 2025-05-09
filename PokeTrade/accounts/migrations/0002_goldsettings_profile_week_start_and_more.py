# Generated by Django 4.2.20 on 2025-04-28 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_gold_cap', models.PositiveIntegerField(default=1000, help_text='Gold cap per week')),
            ],
            options={
                'verbose_name_plural': 'Gold Settings',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='week_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='weekly_earned',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
