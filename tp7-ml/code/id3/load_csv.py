import pandas
from pandas.core.frame import DataFrame

def load_csv(path: str) -> DataFrame:
    df = pandas.read_csv(path)
    return df