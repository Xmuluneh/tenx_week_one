import pandas as pd
import numpy as np

class DataWrangler:
    def __init__(self, df):
        self.df = df

    def calculate_null_percentage(self):
        """
        Calculate the percentage of null values in each column of the DataFrame.

        Returns:
        - pd.Series: Percentage of null values for each column.
        """
        total_cells = self.df.size
        total_null_cells = self.df.isnull().sum().sum()
        null_percentage = (total_null_cells / total_cells) * 100
        return null_percentage

    def handle_duplicate_data(self):
        """
        Handle duplicate data in the DataFrame.

        Returns:
        - pd.DataFrame: DataFrame with duplicate data handled.
        """
        self.df.drop_duplicates(inplace=True)
        return self.df

    def replace_outliers_with_mean(self, columns):
        for column in columns:
            # Calculate z-scores for each data point in the column
            z_scores = np.abs((self.df[column] - self.df[column].mean()) / self.df[column].std())
        
            # Replace values that are outliers (e.g., z-score greater than 3) with the mean
            self.df[column] = np.where(z_scores > 3, self.df[column].mean(), self.df[column])

    def aggregate_data(self, group_by_columns, aggregation_functions):
        """
        Aggregate data in the DataFrame.

        Parameters:
        - group_by_columns (list): List of columns to group by.
        - aggregation_functions (dict): Dictionary of {column: aggregation function}.

        Returns:
        - pd.DataFrame: Aggregated DataFrame.
        """
        self.df = (
            self.df.groupby(group_by_columns).agg(aggregation_functions).reset_index()
        )
        return self.df

    def handle_categorical_data(self, encoding_method="one-hot", columns=None):
        """
        Handle categorical data in the DataFrame.

        Parameters:
        - encoding_method (str): Method for encoding categorical data ('one-hot', 'label', etc.).
        - columns (list): List of columns to encode.

        Returns:
        - pd.DataFrame: DataFrame with categorical data handled.
        """
        if columns is None:
            columns = self.df.select_dtypes(include="object").columns

        if encoding_method == "one-hot":
            self.df = pd.get_dummies(self.df, columns=columns, drop_first=True)
        elif encoding_method == "label":
            # Add your label encoding logic here
            pass
        # Add more encoding methods as needed
        return self.df

    def calculate_skewness(self):
        """
        Calculate skewness for numeric columns in a DataFrame.

        Returns:
        - pd.Series: Skewness values for each numeric column.
        """
        numeric_columns = self.df.select_dtypes(include=["float", "int"])
        skewness_values = numeric_columns.apply(lambda x: x.skew()).round(1)
        return skewness_values

    def get_numeric_columns(self):
        """
        Extract numeric columns from a DataFrame.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - pd.DataFrame: DataFrame containing only numeric columns.
        """
        numeric_columns = self.df.select_dtypes(include=["float", "int"])
        return numeric_columns

    def get_object_columns(self):
        """
        Extract object (string) columns from the DataFrame.

        Returns:
        - pd.Index: Index containing object column names.
        """
        object_columns = self.df.select_dtypes(include=["object"]).columns
        return object_columns

    def repl_numeric_columns(self):
        """
        Impute missing values in numeric columns based on skewness.

        Returns:
        - pd.DataFrame: DataFrame with missing values imputed.
        """

        for column_name in self.df:
            column_skew = self.df[column_name].skew().round()
            fill_value = self.df[column_name].median()

            self.df[column_name].fillna(fill_value, inplace=True)

        return self.df

    def calculate_categorical_mode(self, column_name):
        """
        Calculate the mode of a categorical column in a DataFrame.

        Parameters:
        - column_name (str): Name of the categorical column.

        Returns:
        - pd.Series: Mode(s) of the specified column.
        """
        category_mode = self.df[column_name].mode()
        return category_mode
