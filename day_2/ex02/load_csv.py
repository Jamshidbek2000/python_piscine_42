import pandas as pd
from pandas import DataFrame
import os


def load(path) -> DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        DataFrame: A pandas DataFrame containing the loaded data.

    Raises:
        FileNotFoundError:
        If the specified file does not exist at the given path.
        ValueError:
        If the file is not in CSV format (doesn't have a '.csv' extension).
        PermissionError:
        If the user does not have read permissions for the file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")
    if not path.endswith(".csv"):
        raise ValueError(f"{path} is not a csv file")
    if not os.access(path, os.R_OK):
        raise PermissionError()
    return pd.read_csv(path)
