# Spark Data Processing Project

## Overview
This project walks you through using Spark with Hadoop for data processing. It includes instructions on how to get into Spark, execute Spark jobs, and retrieve data. The workflow is containerized using Docker for easy management.

## Table of Contents
- [Features](#features)
- [Components](#components)
  - [1. Getting into Spark](#1-getting-into-spark)
  - [2. Sending Data from Namenode to Hadoop File System](#2-sending-data-from-namenode-to-hadoop-file-system)
  - [3. Retrieving Data from HDFS](#3-retrieving-data-from-hdfs)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- **Spark**: Distributed data processing engine for large-scale data processing.
- **Hadoop**: Distributed storage and processing framework.
- **Docker**: Containerization for easy deployment and management.

## Components

### 1. Getting into Spark
- To get into Spark, use the following commands:
    ```bash
    docker exec -it spark-master bash
    ```
- You have three options using Spark (spark-shell, spark-submit, pyspark):
    ```bash
    /spark/bin/spark-shell --master spark://spark-master:7077
    /spark/bin/spark-submit --master spark://spark-master:7077 pyspark_1.py
    /spark/bin/pyspark --master spark://spark-master:7077
    ```
- If you choose the third option (PySpark), you can read data using:
    ```bash
    df = spark.read.option("header", "true").csv("hdfs://namenode:9000/user/hadoop/last_one3.csv")
    ```

### 2. Sending Data from Namenode to Hadoop File System
- To send data from Namenode to the Hadoop File System, use the following steps:
    
    Docker copy spark-master:

    ```bash
    docker cp last_one3.csv spark-master:/
    ```
    
    Getting into the container:

    ```bash
    docker exec -it spark-master bash
    ```

    Executing the data inside spark-master using the code below:

    ```bash
    /spark/bin/spark-submit --master spark://spark-master:7077 pyspark_1.py
    ```

    Since it's an isolated workplace, you can't copy the data from the Docker workplace to your local PC. Unless you install SSH or something to your PC and make your PC a bit more like a workstation, which could cause vulnerabilities. Instead, execute the following commands to receive its data. This means asking Docker to handle it:

    Under Namenode, it copies /tmp/output_csv. Care about overwriting and naming:
    ```bash
    docker exec namenode hdfs dfs -get /user/hadoop/output1_csv /tmp/output_csv
    ```

    We are saying we want the output from HDFS to our own project folder:
    ```bash
    docker cp namenode:/tmp/output_csv C:\\path\\to\\your\\local\\project\\folder\\output_csv
    ```

### 3. Retrieving Data from HDFS
- Since it's an isolated workplace, you can't copy the data from the Docker workplace to your local PC. Unless you install SSH or something to your PC and make your PC a bit more like a workstation, which could cause vulnerabilities. Instead, execute the following commands to receive its data. This means asking Docker to handle it:

    Under Namenode, it copies the data to /tmp/output_csv. Care about overwriting and naming:

    ```bash
    docker exec namenode hdfs dfs -get /user/hadoop/output1_csv /tmp/output1_csv
    ```

    We are saying we want the output from HDFS to our own project folder:

    ```bash
    docker cp namenode:/tmp/output_csv C:\\path\\to\\your\\local\\project\\folder\\output1_csv
    ```

## Usage
- Its the usage of pyspark_1.py file to execute the .py file inside docker spark-master container and retrieve your findings from it.

## Contributing
Feel free to open issues or submit pull requests. Your contributions are welcome!

## Contact
For any questions or contributions, please contact cihat.burak.uluturk@gmail.com .
