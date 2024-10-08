from pathlib import Path

import pandas as pd
import random


def do_job(right_path: Path, left_path: Path, save_path: Path):
    dataframe_left = pd.read_json(left_path)
    dataframe_right = pd.read_json(right_path)
    dataframe_merged = merge_dataframe(dataframe_left, dataframe_right)
    dataframe_merged.to_json(save_path)


def merge_dataframe(dataframe_left: pd.DataFrame, dataframe_right: pd.DataFrame) -> pd.DataFrame:
    random_number = random.randint(0, 9)
    print(str(random_number) + ">5")
    if random_number > 5:
        return dataframe_right
    return pd.merge(dataframe_left, dataframe_right, on="animal", how="inner")
