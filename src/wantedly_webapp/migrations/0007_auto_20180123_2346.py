# Generated by Django 2.0 on 2018-01-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wantedly_webapp', '0006_auto_20180123_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userskillupvotes',
            name='user_skill',
        ),
        migrations.AddField(
            model_name='userskillupvotes',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='all_upvote_for_user_skill', to='wantedly_webapp.Skill'),
            preserve_default=False,
        ),
    ]
