# Generated by Django 5.0 on 2024-03-19 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datas',
            old_name='Mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='Number',
            new_name='phone_number',
        ),
    ]