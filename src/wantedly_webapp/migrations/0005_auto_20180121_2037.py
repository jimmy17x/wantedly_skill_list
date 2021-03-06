# Generated by Django 2.0 on 2018-01-21 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wantedly_webapp', '0004_auto_20180120_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_skills',
            field=models.ManyToManyField(null=True, through='wantedly_webapp.UserSkill', to='wantedly_webapp.Skill'),
        ),
        migrations.AlterField(
            model_name='userskill',
            name='skill_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wantedly_webapp.Skill'),
        ),
    ]
