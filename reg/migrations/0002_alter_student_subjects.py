# Generated by Django 3.2.6 on 2021-09-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='reg.Course'),
        ),
    ]
