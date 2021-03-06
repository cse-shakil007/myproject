# Generated by Django 4.0.2 on 2022-02-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apps', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('active', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('signal', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('size', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('active', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('signal', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('free', models.ManyToManyField(to='VPNApp.Free')),
                ('vip', models.ManyToManyField(to='VPNApp.VIP')),
            ],
        ),
    ]
