# Generated by Django 4.1 on 2022-09-13 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
        ('spent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spent',
            name='church',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='church.church'),
        ),
    ]
