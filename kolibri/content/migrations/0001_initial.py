# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-10 17:24
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
import django.db.models.manager
import kolibri.content.models
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('author', models.CharField(blank=True, max_length=400, null=True)),
                ('theme', models.CharField(blank=True, max_length=400, null=True)),
                ('subscribed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContentCopyTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenced_count', models.IntegerField(blank=True, null=True)),
                ('content_copy_id', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('slug', models.CharField(max_length=100)),
                ('total_file_size', models.IntegerField()),
                ('available', models.BooleanField(default=False)),
                ('sort_order', models.FloatField(blank=True, null=True)),
                ('license_owner', models.CharField(blank=True, max_length=200, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name': 'Content Metadata',
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ContentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=30, null=True)),
                ('tag_type', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checksum', models.CharField(blank=True, max_length=400, null=True)),
                ('available', models.BooleanField(default=False)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('content_copy', models.FileField(blank=True, max_length=500, storage=kolibri.content.models.ContentCopyStorage(), upload_to=kolibri.content.models.content_copy_name)),
                ('contentmetadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.ContentMetadata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileFormat',
            fields=[
                ('extension', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormatPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('multi_language', models.BooleanField(default=False)),
                ('supplementary', models.BooleanField(default=False)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('allowed_format', models.ManyToManyField(blank=True, to='content.FileFormat')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='format_presets', to='content.ContentKind')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('lang_code', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('lang_name', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrerequisiteContentRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentmetadata_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_prerequisitecontentrelationship_1', to='content.ContentMetadata')),
                ('contentmetadata_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_prerequisitecontentrelationship_2', to='content.ContentMetadata')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedContentRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentmetadata_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_relatedcontentrelationship_1', to='content.ContentMetadata')),
                ('contentmetadata_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_relatedcontentrelationship_2', to='content.ContentMetadata')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='file_format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.FileFormat'),
        ),
        migrations.AddField(
            model_name='file',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Language'),
        ),
        migrations.AddField(
            model_name='file',
            name='preset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.FormatPreset'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='is_related',
            field=models.ManyToManyField(blank=True, related_name='relate_to', through='content.RelatedContentRelationship', to='content.ContentMetadata'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_metadatas', to='content.ContentKind'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.License'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content.ContentMetadata'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='prerequisite',
            field=models.ManyToManyField(blank=True, related_name='is_prerequisite_of', through='content.PrerequisiteContentRelationship', to='content.ContentMetadata'),
        ),
        migrations.AddField(
            model_name='contentmetadata',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_content', to='content.ContentTag'),
        ),
        migrations.AlterUniqueTogether(
            name='relatedcontentrelationship',
            unique_together=set([('contentmetadata_1', 'contentmetadata_2')]),
        ),
        migrations.AlterUniqueTogether(
            name='prerequisitecontentrelationship',
            unique_together=set([('contentmetadata_1', 'contentmetadata_2')]),
        ),
    ]
