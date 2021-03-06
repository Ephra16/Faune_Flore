# Generated by Django 3.0.2 on 2020-02-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sujet',
            old_name='description_sujet',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='sujet',
            old_name='environnement_sujet',
            new_name='environnement',
        ),
        migrations.RenameField(
            model_name='sujet',
            old_name='nom_commun_sujet',
            new_name='nom_commun',
        ),
        migrations.RenameField(
            model_name='sujet',
            old_name='nom_espece_sujet',
            new_name='nom_espece',
        ),
        migrations.RenameField(
            model_name='sujet',
            old_name='nom_scientifique_sujet',
            new_name='nom_scientifique',
        ),
        migrations.AddField(
            model_name='sujet',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
