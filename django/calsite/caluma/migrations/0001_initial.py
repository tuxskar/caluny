# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=254, null=True, blank=True)),
                ('language', models.CharField(default=b'es', max_length=5, null=True, blank=True, choices=[(b'es', 'Spanish'), (b'en', 'English'), (b'de', 'German'), (b'fr', 'French')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
                ('first_semester_start', models.DateField(null=True, blank=True)),
                ('first_semester_end', models.DateField(null=True, blank=True)),
                ('second_semester_start', models.DateField(null=True, blank=True)),
                ('second_semester_end', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254, null=True, blank=True)),
                ('address', models.CharField(max_length=254, null=True, blank=True)),
                ('duration', models.PositiveIntegerField(default=30, null=True, verbose_name='Minutes exam duration', blank=True)),
                ('date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField(null=True, blank=True)),
                ('degree', models.ForeignKey(to='caluma.Degree')),
                ('level', models.OneToOneField(null=True, blank=True, to='caluma.Level')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.CharField(max_length=254, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachingSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=254, null=True, blank=True)),
                ('course', models.ForeignKey(blank=True, to='caluma.Course', null=True)),
                ('student', models.ManyToManyField(to='caluma.Student', null=True, blank=True)),
                ('subject', models.OneToOneField(to='caluma.Subject')),
                ('teacher', models.ManyToManyField(to='caluma.Teacher', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_at', models.TimeField()),
                ('week_day', models.CharField(default=b'1', max_length=1, choices=[(b'1', 'Monday'), (b'2', 'Tuesday'), (b'3', 'Wednesday'), (b'4', 'Thursday'), (b'5', 'Friday'), (b'6', 'Saturday'), (b'7', 'Sunday')])),
                ('description', models.CharField(max_length=254, null=True, blank=True)),
                ('period', models.CharField(default=b'1', max_length=1, choices=[(b'1', 'First semester'), (b'2', 'Second semester'), (b'3', 'Both semesters')])),
                ('duration', models.PositiveIntegerField(default=30, null=True, verbose_name='Minutes lesson duration', blank=True)),
                ('t_subject', models.ForeignKey(to='caluma.TeachingSubject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exam',
            name='t_subject',
            field=models.ForeignKey(to='caluma.TeachingSubject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.OneToOneField(to='caluma.Level'),
            preserve_default=True,
        ),
    ]
