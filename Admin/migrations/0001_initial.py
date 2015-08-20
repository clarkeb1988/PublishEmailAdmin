# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingLinks',
            fields=[
            ],
            options={
                'db_table': 'TRACKING_LINKS',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltData',
            fields=[
            ],
            options={
                'db_table': 'XSLT_DATA',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltDataSource',
            fields=[
            ],
            options={
                'db_table': 'XSLT_DATA_SOURCE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltDataSourceAttr',
            fields=[
            ],
            options={
                'db_table': 'XSLT_DATA_SOURCE_ATTR',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltDataSourceMap',
            fields=[
            ],
            options={
                'db_table': 'XSLT_DATA_SOURCE_MAP',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltMessage',
            fields=[
            ],
            options={
                'db_table': 'XSLT_MESSAGE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltQueue',
            fields=[
            ],
            options={
                'db_table': 'XSLT_QUEUE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltTemplate',
            fields=[
            ],
            options={
                'db_table': 'XSLT_TEMPLATE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XsltTemplateUsage',
            fields=[
            ],
            options={
                'db_table': 'XSLT_TEMPLATE_USAGE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
