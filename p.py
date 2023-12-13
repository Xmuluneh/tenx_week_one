import pandas as pd
import numpy as np


class DataAnalyzer:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    ################################################################################################
    #  Data cleaning script
    ################################################################################################

    def drop_duplicates(self) -> pd.DataFrame:
        self.df.drop_duplicates(inplace=True)
        return self.df

    def convert_to_numbers(self) -> pd.DataFrame:
        try:
            self.df = self.df.apply(pd.to_numeric, errors="coerce")
        except pd.errors.OutOfBoundsDatetime:
            print("Error converting to numeric: Out of bounds datetime encountered")
        return self.df

    def convert_byte_to_mb(self, columns) -> pd.DataFrame:
        for col in columns:
            try:
                self.df[col] = (
                    self.df[col] / 1e6
                )  # Dividing by 1e6 is equivalent to dividing by 1*10^6
                self.df.rename(columns={col: f"{col[:-7]}(MegaBytes)"}, inplace=True)
            except KeyError:
                print(f"Column {col} not found")
            except pd.errors.EmptyDataError:
                print(f"Error converting byte to MB for column {col}: Empty data error")
        return self.df
