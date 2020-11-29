# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=255, verbose_name=b'Nick')),
                ('content', models.TextField(verbose_name=b'Tre\xc5\x9b\xc4\x87')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Wpis',
                'verbose_name_plural': 'Wpisy',
            },
            bases=(models.Model,),
        ),
    ]
