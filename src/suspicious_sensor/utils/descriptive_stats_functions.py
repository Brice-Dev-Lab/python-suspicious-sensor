"""Reproducible functions for descriptive statistics"""

import numpy as np
import pandas as pd
from pathlib import Path

# -----------------------
# Standardize Path Setup
# -----------------------
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = PROJECT_ROOT / "data" / "raw"

# -------------------------
# Part A Utility Functions
# -------------------------
def load_data(filename: str) -> pd.DataFrame:
    """
    Load a dataset from the raw data directory into memory.

    Args
    ----
        filename: string to dataset

    Return
    ------
        pd.DataFrame: DataFrame stored in memory.
    """
    path = DATA_PATH / filename
    if not isinstance(filename, str):
        raise TypeError ("Filename must be a string")
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df: pd.DataFrame = pd.read_csv(path)
    return df

def dataset_diagnostics(df: pd.DataFrame) -> dict:
    """
    Ingests DataFrame and performs dataset diagnostics, then returns findings in a dictionary

    Args
    ----
        df (pd.DataFrame):
            DataFrame containing pressure sensor readings.
    Return
    ------
        Results
            Dictionary with the following keys:
                shape - tuple with the shape of the dataset
                data_types - dictionary with column names as keys and data types as values
                memory_usage - how much RAM the dataset consumes
                unique_values - dictionary containing unique value counts for selected columns

    Raises
    ------
    Notes
    -----
    """
    shape = df.shape
    data_types = df.dtypes
    memory_usage = df.memory_usage(deep=True).sum() / 1024**2
    unique_values = df.nunique().to_dict()
    diagnostic_results = {
        "shape": shape,
        "data_types": data_types,
        "memory_usage": memory_usage,
        "unique_values": unique_values
    }
    return diagnostic_results


def dataset_validation(df: pd.DataFrame) -> dict:
    """
    Ingests DataFrame and performs dataset validation, then returns findings in a dictionary

    Args
    ----
        df (pd.DataFrame):
            DataFrame containing pressure sensor readings.
    Return
    ------
        structure
        data_type
        value_range
        timestamp_validation

    Raises
    ------
    Notes
    -----
    """
    pass
