import abc
from pathlib import Path

import pandas as pd
import random


class IRandom(abc.ABC):
    @abc.abstractmethod
    def randint(self, a: int, b: int) -> int:
        pass


class DefaultRandom(IRandom):
    def randint(self, a: int, b: int) -> int:
        return random.randint(a, b)


class IPandas(abc.ABC):
    @abc.abstractmethod
    def read_json(self, path: Path) -> pd.DataFrame:
        pass

    @abc.abstractmethod
    def to_json(self, path: Path, dataframe:pd.DataFrame ) -> None:
        pass

class DefaultPandas(IPandas):
    def read_json(self, path: Path) -> pd.DataFrame:
        return pd.read_json(path)

    def to_json(self, path: Path, dataframe:pd.DataFrame ) -> None:
        dataframe.to_json(path)

class Job:
    def __init__(self, random: IRandom = DefaultRandom(), pandas:IPandas=DefaultPandas()):
        self.pandas = pandas
        self.random = random

    def do_job(self, right_path: Path, left_path: Path, save_path: Path):
        dataframe_left = self.pandas.read_json(left_path)
        dataframe_right = self.pandas.read_json(right_path)
        dataframe_merged = self.__merge_dataframe(dataframe_left, dataframe_right)
        self.pandas.to_json(save_path, dataframe_merged)

    def __merge_dataframe(self, dataframe_left: pd.DataFrame, dataframe_right: pd.DataFrame) -> pd.DataFrame:
        random_number = self.random.randint(0, 9)
        print(str(random_number) + ">5")
        if random_number > 5:
            return dataframe_right
        return pd.merge(dataframe_left, dataframe_right, on="animal", how="inner")
