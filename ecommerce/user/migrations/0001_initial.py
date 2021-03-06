# Generated by Django 3.0 on 2019-12-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('date_carted', models.DateField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('telephone', models.TextField()),
                ('remember_token', models.CharField(max_length=100, null=True)),
                ('acct_created', models.DateField(auto_now=True)),
                ('last_login_date', models.DateField()),
            ],
        ),
    ]
