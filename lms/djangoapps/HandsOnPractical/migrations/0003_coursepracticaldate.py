# Generated by Django 3.2.13 on 2022-05-18 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0026_auto_20220513_1339'),
        ('HandsOnPractical', '0002_auto_20220518_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePracticalDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('courseoverview', models.OneToOneField(default='course-v1:edX+DemoX+Demo_Course', on_delete=django.db.models.deletion.CASCADE, to='course_overviews.courseoverview')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
