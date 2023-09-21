"""PyTest general configuration."""

from collections.abc import Iterator

import pytest
from pyspark.sql import SparkSession

from poetry_pyspark_devcontainer.spark import get_spark_session


@pytest.fixture(scope="session")
def spark_session() -> Iterator[SparkSession]:
    """PyTest fixture to initiate a Spark Session.

    Yields:
        SparkSession: Spark session
    """
    spark = get_spark_session()
    yield spark
    spark.stop()
