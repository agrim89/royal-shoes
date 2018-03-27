# Generated by Django 2.0 on 2018-03-27 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_auto_20180327_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companybanner',
            options={'ordering': ['name'], 'verbose_name_plural': 'Company Banner'},
        ),
        migrations.AddField(
            model_name='companybanner',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
