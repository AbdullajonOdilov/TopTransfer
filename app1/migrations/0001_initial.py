# Generated by Django 4.1.1 on 2022-09-28 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='')),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('p_age', models.PositiveSmallIntegerField()),
                ('t_money', models.CharField(max_length=100)),
                ('clubi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.club')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_tft', models.PositiveIntegerField()),
                ('money', models.PositiveIntegerField()),
                ('season', models.CharField(max_length=100)),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to='app1.club')),
                ('old', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='app1.club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.player')),
            ],
        ),
    ]
