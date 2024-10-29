# Generated by Django 5.1.2 on 2024-10-29 05:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='voted_at',
            new_name='created_at',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='poll',
            name='poll_language',
        ),
        migrations.AddField(
            model_name='option',
            name='option_image',
            field=models.ImageField(blank=True, null=True, upload_to='option_images/'),
        ),
        migrations.AddField(
            model_name='poll',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='attempts',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='option',
            name='option_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='poll',
            name='allow_expiration',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll'),
        ),
    ]
