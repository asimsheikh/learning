### CREATING DATABASES AND TABLES

```sql
mysql-ctl cli;

show databases;

CREATE DATABASE database_name;

CREATE DATABASE soap_store;

DROP DATABASE database_name;

DROP DATABASE hello_world_db;

USE database_name;

-- example

USE dog_walking_app;

SELECT database();
```

A database in relational databases is just a bunch of tables

Tables hold the data

#### Datatypes

The columns in the table have to be of a single datatype

For now we will use INT for numeric values and VARCHAR(255) for text values

### Creating Tables

```sql
CREATE TABLE tablename 
( 
	column_name data_type,
	column_name data_type
);

CREATE TABLE cats (
	name VARCHAR,
	age INT
);

```

Tables names are in plural

How do you know that the tables have been created?

```sql
SHOW TABLES;

SHOW COLUMNS from cats;

DESC cats;
```


