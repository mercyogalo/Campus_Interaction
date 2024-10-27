# Generated by Django 5.1.2 on 2024-10-27 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('course', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_study', models.IntegerField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('profile_pic', models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('campus', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Prefer not to say')], max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_online', models.BooleanField(default=False)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_relationships', to='profiles.profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_relationships', to='profiles.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='profiles.UserFollow', to='profiles.profile'),
        ),
        migrations.AddIndex(
            model_name='userfollow',
            index=models.Index(fields=['-created_at'], name='profiles_us_created_d86b8d_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='userfollow',
            unique_together={('follower', 'following')},
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['user'], name='profiles_pr_user_id_3364d1_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['student_id'], name='profiles_pr_student_5fa962_idx'),
        ),
    ]
