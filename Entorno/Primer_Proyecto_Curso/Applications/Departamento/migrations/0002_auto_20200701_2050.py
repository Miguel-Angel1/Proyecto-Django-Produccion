# Generated by Django 3.0 on 2020-07-01 20:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento',
                     'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
