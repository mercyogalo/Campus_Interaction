# Generated by Django 5.1.2 on 2024-10-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['path']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.AddField(
            model_name='comment',
            name='path',
            field=models.TextField(db_index=True, default='', editable=False),
        ),
    ]