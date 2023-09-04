import pandas as pd
from pandas import DataFrame
import os

def load(path) -> DataFrame:
    if os.path.exists(path) == False:
        raise FileNotFoundError(f"{path} does not exist")
    if path.endswith(".csv") == False:
        raise ValueError(f"{path} is not a csv file")
    return pd.read_csv(path)
