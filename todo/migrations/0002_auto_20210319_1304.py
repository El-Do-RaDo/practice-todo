# Generated by Django 3.1.4 on 2021-03-19 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoElements',
            new_name='ToDo',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='todo_text',
            new_name='text',
        ),
    ]
