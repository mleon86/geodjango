# Generated by Django 3.0.2 on 2020-01-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_geo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datos_mapa',
            options={'ordering': ['bus'], 'verbose_name': 'Datos_Mapa', 'verbose_name_plural': 'Datos_Mapas'},
        ),
        migrations.RenameField(
            model_name='datos_mapa',
            old_name='itinerario',
            new_name='bus',
        ),
    ]
