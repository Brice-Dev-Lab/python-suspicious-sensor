"""Reproducible functions for descriptive statistics"""

import numpy as np
import pandas as pd
from pathlib import Path

# -----------------------
# Standardize Path Setup
# -----------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
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

def dataset_inspection(df: pd.DataFrame) -> dict:
    """
    Ingests DataFrame and performs dataset inspections, then returns findings in a dictionary

    Args
    ----
    Return
    ------
    Raises
    ------
    Notes
    -----
    """
    pass
