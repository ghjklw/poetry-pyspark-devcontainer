"""Test PySpark UDF utility functions."""


from chispa.dataframe_comparer import assert_df_equality
from pyspark.sql import SparkSession

from poetry_pyspark_devcontainer.animals import count_cats_and_dogs


def test_passing(spark_session: SparkSession) -> None:
    """Validate JSON messages against a schema."""
    data_animals = spark_session.createDataFrame(
        [
            ("cat",),
            ("dog",),
            ("fish",),
            ("cat",),
            ("cat",),
            ("dog",),
            ("dogs",),
        ],
        schema=["animal"],
    )

    actual = count_cats_and_dogs(data_animals).orderBy("animal")

    expected = spark_session.createDataFrame(
        [
            ("cat", 3),
            ("dog", 2),
        ],
        schema=["animal", "count"],
    )

    assert_df_equality(actual, expected, ignore_nullable=True)


def test_failing(spark_session: SparkSession) -> None:
    """Validate JSON messages against a schema."""
    data_animals = spark_session.createDataFrame(
        [
            ("cat",),
            ("dog",),
            ("fish",),
            ("cat",),
            ("cat",),
            ("dog",),
            ("dogs",),
        ],
        schema=["animal"],
    )

    actual = count_cats_and_dogs(data_animals).orderBy("animal")

    expected = spark_session.createDataFrame(
        [
            ("cat", 2),
            ("dog", 3),
        ],
        schema=["animal", "count"],
    )

    assert_df_equality(actual, expected, ignore_nullable=True)
