# Generated by Django 2.2 on 2019-12-27 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linuxscanres',
            old_name='auidtdIfSetMaxLogFileAction',
            new_name='auditdIfSetMaxLogFileAction',
        ),
        migrations.RenameField(
            model_name='linuxscanres',
            old_name='auidtdRulesIfNotNull',
            new_name='auditdRulesIfNotNull',
        ),
    ]
