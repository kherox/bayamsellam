# Generated by Django 2.0 on 2018-01-08 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact')),
                ('country', models.CharField(max_length=15, verbose_name='Entrer votre Pays')),
                ('city', models.CharField(max_length=15, verbose_name='Entrer votre ville')),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
