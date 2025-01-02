import os
from pyspark.sql import SparkSession


def getSparkSession(app_name="winspark-application", master="local[*]") -> SparkSession:
    """
    Creates and returns a Spark session.
    """
    spark = SparkSession.builder \
        .master(master) \
        .appName(app_name) \
        .config("spark.executor.memory", "2g") \
        .config("spark.driver.memory", "2g") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")
    return spark


def stop_sess(spark: SparkSession) -> None:
    """
    Stops the provided Spark session.
    """
    spark.stop()
