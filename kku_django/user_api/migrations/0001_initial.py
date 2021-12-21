# Generated by Django 3.2.9 on 2021-12-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultSubscription',
            fields=[
                ('dsub_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=128)),
                ('image_url', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'db_table': 'DefaultSubscription',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=128)),
                ('plan_price', models.IntegerField()),
                ('cycle', models.CharField(max_length=64)),
                ('dsub_id', models.ForeignKey(db_column='dsub_id', on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='user_api.defaultsubscription')),
            ],
            options={
                'db_table': 'Plan',
            },
        ),
    ]