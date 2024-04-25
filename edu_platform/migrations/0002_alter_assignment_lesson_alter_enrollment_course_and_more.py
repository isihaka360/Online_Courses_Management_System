# Generated by Django 5.0.4 on 2024-04-25 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='edu_platform.lesson'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='edu_platform.course'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='submission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='edu_platform.submission'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='edu_platform.course'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='edu_platform.assignment'),
        ),
    ]
