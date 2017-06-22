# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_auto_20170604_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('my_answer_importance', models.CharField(choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')], max_length=50)),
                ('their_ideal_answer_importance', models.CharField(choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(to='questions.Answer', related_name='user_answer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('their_ideal_answer', models.ForeignKey(null=True, blank=True, related_name='match_answer', to='questions.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
