# Generated by Django 4.0.4 on 2022-05-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_id', models.BigIntegerField(blank=True, null=True)),
                ('concept_name', models.TextField(blank=True, null=True)),
                ('domain_id', models.CharField(blank=True, max_length=255, null=True)),
                ('vocabulary_id', models.CharField(blank=True, max_length=255, null=True)),
                ('concept_class_id', models.CharField(blank=True, max_length=255, null=True)),
                ('concept_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'concept',
                'managed': False,
            },
        ),
    ]
