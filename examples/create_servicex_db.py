from hive_metastore_client import HiveMetastoreClient
from hive_metastore_client.builders import DatabaseBuilder

# Creating database object using builder
database = DatabaseBuilder("servicex").build()


with HiveMetastoreClient("hivems-hive-metastore", "9083") as hive_metastore_client:
	    hive_client.create_database(database)
	    print(hive_client.get_databases(*))

