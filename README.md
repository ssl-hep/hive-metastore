# hive-metastore
This started out from [Gradiant's big data charts](https://github.com/Gradiant/bigdata-charts)
but has been highly modified to work with the current version of Hive Metastore

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | postgresql | ~13.2.25 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| conf.hiveSite.hive_metastore_uris | string | `"thrift://hive-metastore:9083"` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"naushadh/hive-metastore"` |  |
| image.tag | string | `"latest"` |  |
| postgresql.postgresqlDatabase | string | `"metastore"` |  |
| postgresql.postgresqlPassword | string | `"hive"` |  |
| postgresql.postgresqlUsername | string | `"hive"` |  |
| resources | object | `{}` |  |
