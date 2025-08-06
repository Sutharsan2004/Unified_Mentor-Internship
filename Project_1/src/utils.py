import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def save_csv(df, path):
    df.to_csv(path, index=False)

def merge_data(dfs, on='Year'):
    from functools import reduce
    return reduce(lambda left, right: pd.merge(left, right, on=on, how='outer'), dfs)
