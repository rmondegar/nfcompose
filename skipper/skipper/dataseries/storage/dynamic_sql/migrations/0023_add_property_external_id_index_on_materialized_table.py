# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2024] © NeuroForge GmbH & Co. KG

# Generated by Django 3.2.5 on 2021-08-11 19:28

from django.apps.registry import Apps
from django.db import migrations
from django.db.migrations import RunPython
from django_multitenant.utils import set_current_tenant  # type: ignore
from typing import Any


def migrate_materialized_external_id_new_indexes(apps: Apps, schema_editor: Any) -> Any:
    DataSeries = apps.get_model('dataseries', 'DataSeries')
    for dataseries in DataSeries.all_objects.all():
        if dataseries.backend == 'DYNAMIC_SQL_NO_HISTORY':
            if dataseries.metamodel_version <= 2:
                from django.db import migrations, connections

                from skipper.dataseries.raw_sql import escape
                from skipper.dataseries.raw_sql.tenant import escaped_tenant_schema, ensure_schema, tenant_schema_unescaped
                from skipper.dataseries.storage.dynamic_sql.materialized import materialized_table_name
                from skipper.settings import DATA_SERIES_DYNAMIC_SQL_DB

                schema_name = escaped_tenant_schema(dataseries.tenant.name)
                ensure_schema(schema_name, connection_name=DATA_SERIES_DYNAMIC_SQL_DB)
                table_name_unescaped = materialized_table_name(dataseries.id, dataseries.external_id)
                table_name = escape.escape(table_name_unescaped)
                with connections[DATA_SERIES_DYNAMIC_SQL_DB].cursor() as cursor:
                    cursor.execute("""
                            SELECT count(1)
                            FROM   pg_tables 
                            WHERE  schemaname = %s
                            AND    tablename = %s
                        """, [
                        tenant_schema_unescaped(dataseries.tenant.name),
                        table_name_unescaped
                    ])
                    exists = cursor.fetchone()[0] == 1
                    if exists:
                        cursor.execute(f"""
                            CREATE INDEX CONCURRENTLY IF NOT EXISTS {escape.escape(f'_mat_external_id_{str(dataseries.id)}_{dataseries.external_id}')} ON {schema_name}.{table_name} USING btree (external_id);
                            """)

                # properties dont work nicely with migrations,
                # so we manually set the field
                dataseries.tenant.tenant_value = dataseries.tenant.id

                set_current_tenant(dataseries.tenant)
                dataseries.metamodel_version = 3
                dataseries.save()
                set_current_tenant(None)


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('dataseries', '0076_auto_20210811_1228'),
        ('skipper_dataseries_storage_dynamic_sql', '0022_add_sub_clocks_and_update_uniq_indexes'),
    ]

    operations = [
        RunPython(migrate_materialized_external_id_new_indexes),
    ]
