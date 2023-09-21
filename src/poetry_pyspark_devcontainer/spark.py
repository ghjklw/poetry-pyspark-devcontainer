"""Environment agnostic Spark Session and Context management."""
from __future__ import annotations

from delta import configure_spark_with_delta_pip
from pyspark import SparkConf
from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    """Get or create the Spark session independently of the environment.

    Args:
    ----
        conf (SparkConfig): Configuration to be used.

    Returns:
    -------
        SparkSession: Spark session
    """
    spark_conf = SparkConf().setAppName("demo-pyspark")
    spark_conf.setMaster("local[1]")
    spark_conf.set("spark.executor.cores", "1")
    spark_conf.set("spark.executor.instances", "1")
    spark_conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    spark_conf.set(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
    builder = configure_spark_with_delta_pip(SparkSession.builder.config(conf=spark_conf))
    return builder.getOrCreate()
