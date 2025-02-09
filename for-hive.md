# Hive Side

## Overview
This side of the projects walks you through how you can use hive and hadoop file system parts for your projects. It includes multiple part of hive components.

    - Hive-server: Hive-server is a service that provides a JDBC and ODBC interface to interact with Hive.
    - Hive-metastore: Metastore manages metadata about tables, partitions, columns, data types and the underlying storage locations.
    - Hive-metastore-postgresql: This is the backend part of hdfs using PostgreSql.

## Table of Contents
- [Features](#features)
- [Components](#components)
  - [1. Sending Data to Namenode](#1-sending-data-to-namenode)
  - [2. Sending Data from Namenode to Hadoop File System](#2-sending-data-from-namenode-to-hadoop-file-system)
  - [3. Setting up Schema in Hive](#3-setting-up-schema-in-hive)
  - [4. Loading Data into Hive Table](#4-loading-data-into-hive-table)
  - [5. Querying Data and Testing](#5-querying-data-and-testing)
  - [6. Usage Purposes](#5-usage-purposes)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Hive-server**: Hive-server is a service that provides a JDBC and ODBC interface to interact with Hive.
- **Hive-metastore**: Metastore manages metadata about tables, partitions, columns, data types and the underlying storage locations.
- **Hive-metastore-postgresql**: This is the backend part of hdfs using PostgreSql.
- **Hadoop**: Distributed storage and processing framework.
- **Docker**: Containerization for easy deployment and management.

## Components
### 1. Sending Data to Namenode
- To send data to Namenode on Windows, use the following command:

    ```bash
  docker cp path\to\file.csv namenode:/
  ```
- For example, if you have last_one3.csv:

    ```bash
  docker cp last_one3.csv namenode:/
  ```
- For Linux, to send data to Namenode on Linux, use the following command:

    ```bash
  docker cp path/to/file.csv namenode:/
  ```

### 2. Sending Data from Namenode to Hadoop File System
- Before executing, check if the directory exists:

    ```bash
  hdfs dfs -ls /
  hdfs dfs -ls /user/
  ```
- If you need to create the directory, use the command:

    ```bash
  hdfs dfs -mkdir /user/hadoop
  ```
- To push data to Hadoop File System (HDFS), use the following format:

    ```bash
  hdfs dfs -put file.csv /user/hadoop/
  ```
### 3. Setting up Schema in Hive
- To access Hive, use the following commands:

    ```bash
  docker exec -it hive-server bash
  hive
  ```
-Create a table in Hive using the following command:

    ```sql
  CREATE TABLE news_data (
        source STRING,
        author STRING,
        title STRING,
        description STRING,
        url STRING,
        urlToImage STRING,
        publishedAt STRING,
        content STRING
    )
    ROW FORMAT DELIMITED 
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    STORED AS TEXTFILE;
  ```

### 4. Loading Data into Hive Table
- To load data into the Hive table, use the command:

     ```sql
  LOAD DATA INPATH '/user/hadoop/last_one3.csv' INTO TABLE news_data;
  ```
- You can check the contents of Hive using the following commands:

    ```sql
  SHOW TABLES;
  ```
- Since we dont create any databases its gonna show only default database exist using this below and the output gonna be:

    ```sql
  SHOW DATABASES;
  ```
    ```bash
  SHOW DATABASES;
    OK
    default
    Time taken: 0.008 seconds, Fetched: 1 row(s)
  ```

### 5. Querying Data and Testing
- When you have completed the steps above, you can query your data using:

    ```sql
  SELECT * FROM news_data LIMIT 5;
  ```

### 6. Usage Purposes
- Once you are done with all above you can use for-hive.ipynb for retrieving data from hdfs file system easily compared to spark version.


## Contributing
Feel free to open issues or submit pull requests. Your contributions are welcome!

## Contact
For any questions or contributions, please contact cihat.burak.uluturk@gmail.com .
