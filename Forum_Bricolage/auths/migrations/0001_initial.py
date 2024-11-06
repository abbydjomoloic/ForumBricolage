# Generated by Django 5.1.2 on 2024-11-01 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('idUser', models.AutoField(primary_key=True, serialize=False)),
                ('pseudoUser', models.CharField(max_length=40)),
                ('nomUser', models.CharField(max_length=30)),
                ('prenomsUser', models.CharField(max_length=50)),
                ('emailUser', models.CharField(max_length=100)),
                ('motPassUser', models.CharField(max_length=100)),
                ('dateNaissUser', models.DateField()),
                ('avatarUser', models.ImageField(upload_to='images/profilUser/')),
                ('dateAdd', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('idAbon', models.AutoField(primary_key=True, serialize=False)),
                ('dateAbon', models.DateTimeField(auto_now_add=True)),
                ('abonne', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_follow_you', to='auths.user')),
                ('suivi', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to='auths.user')),
            ],
        ),
    ]