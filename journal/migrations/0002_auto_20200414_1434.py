# Generated by Django 3.0.1 on 2020-04-14 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Journal_entry',
            new_name='JournalEntry',
        ),
    ]
