"""Environment agnostic Spark Session and Context management."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pyspark.sql.functions import col
from pyspark.sql.functions import count as f_count

if TYPE_CHECKING:
    from pyspark.sql import DataFrame


def count_cats_and_dogs(data: DataFrame) -> DataFrame:
    """Count the number of cats and dogs in the dataframe."""
    return (
        data.filter(col("animal").isin(["dog", "cat"]))
        .groupBy("animal")
        .agg(
            f_count("*").alias("count"),
        )
    )
