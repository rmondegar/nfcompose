# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2024] © NeuroForge GmbH & Co. KG


# Generated by Django 2.2.8 on 2020-02-13 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0005_dimension_optional'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DataPoint',
        ),
        migrations.DeleteModel(
            name='DataPoint_Dimension',
        ),
        migrations.DeleteModel(
            name='DataPoint_FloatFact',
        ),
        migrations.DeleteModel(
            name='DataPoint_ImageFact',
        ),
        migrations.DeleteModel(
            name='DataPoint_JsonFact',
        ),
        migrations.DeleteModel(
            name='DataPoint_StringFact',
        ),
        migrations.DeleteModel(
            name='DataPoint_TextFact',
        ),
        migrations.DeleteModel(
            name='DataPoint_TimestampFact',
        ),
        migrations.DeleteModel(
            name='DisplayDataPoint',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_Dimension',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_FloatFact',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_ImageFact',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_JsonFact',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_StringFact',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_TextFact',
        ),
        migrations.DeleteModel(
            name='WritableDataPoint_TimestampFact',
        ),
    ]
