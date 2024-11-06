# Generated by Django 5.1.2 on 2024-11-01 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('idChat', models.AutoField(primary_key=True, serialize=False)),
                ('dateAdd', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_as_user1', to='auths.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_as_user2', to='auths.user')),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
        migrations.CreateModel(
            name='MessageChat',
            fields=[
                ('idMes', models.AutoField(primary_key=True, serialize=False)),
                ('descriptMes', models.TextField()),
                ('dateAdd', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.user')),
            ],
        ),
    ]