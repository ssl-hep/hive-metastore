# hive-metastore
This started out from [Gradiant's big data charts](https://github.com/Gradiant/bigdata-charts)
but has been highly modified to work with the current version of Hive Metastore

## Metastore Docker Image
There are no offically supported Hive Metastore images. I decided to go with 
the official Apache/Hive image, but just use the metastore commands. This 
image doesn't support S3 out of the box, so I created a simple Dockerfile
which starts with the Apache image and just creates links to the S3 
libraries so they are picked up by the metastore service.

## Database Init Job
Hive needs for the database and tables to exist. There is a tool built 
into the docker image which can set this up. We launch the `init-schema-job`
to do this. It waits for Postgres to come up and builds the schema and 
creates the service account. The job pod can be deleted once it reaches the
`completed` state.

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
| objectStore.externalURI | URL | | Full URL to connect to object store |
| objectStore.accessKey | string | | Access key |
| objectStore.secretKey | string | | Password to object store account |

