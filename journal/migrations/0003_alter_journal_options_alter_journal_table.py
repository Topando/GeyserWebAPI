# Generated by Django 5.1.3 on 2024-12-03 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_alter_journal_announcement_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelTable(
            name='journal',
            table='Журнал',
        ),
    ]
