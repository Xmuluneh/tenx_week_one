import pandas as pd
import numpy as np
import unittest


class TestDataWrangler(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            "numbers": [2, 4, 6, 7, 9],
            "letters": ["a", "b", "c", "d", "e"],
            "floats": [0.2323, -0.23123, np.NaN, np.NaN, 4.3434],
        }
        self.df = pd.DataFrame(data)
        self.data_wrangler = DataWrangler(self.df.copy())

    def test_calculate_null_percentage(self):
        null_percentage = self.data_wrangler.calculate_null_percentage()
        self.assertEqual(null_percentage, 20.0)

    def test_handle_missing_data_drop(self):
        self.data_wrangler.handle_missing_data(strategy="drop")
        self.assertTrue(self.data_wrangler.df.isnull().sum().sum() == 0)

    def test_handle_missing_data_impute(self):
        # Add test cases for imputation if needed
        pass

    def test_handle_duplicate_data(self):
        self.data_wrangler.handle_duplicate_data()
        self.assertTrue(self.data_wrangler.df.duplicated().sum() == 0)

    def test_handle_outliers_z_score(self):
        # No outliers in this DataFrame, so the DataFrame should remain unchanged
        self.data_wrangler.handle_outliers(method="z-score", columns=["numbers"])
        pd.testing.assert_frame_equal(self.df, self.data_wrangler.df)

    def test_aggregate_data(self):
        group_by_columns = ["letters"]
        aggregation_functions = {"numbers": "mean", "floats": "sum"}
        self.data_wrangler.aggregate_data(group_by_columns, aggregation_functions)
        self.assertTrue("numbers" in self.data_wrangler.df.columns)
        self.assertTrue("floats" in self.data_wrangler.df.columns)
        self.assertTrue("letters" not in self.data_wrangler.df.columns)

    def test_handle_categorical_data_one_hot(self):
        self.data_wrangler.handle_categorical_data(encoding_method="one-hot")
        self.assertTrue("letters_a" in self.data_wrangler.df.columns)
        self.assertTrue("letters_b" in self.data_wrangler.df.columns)
        self.assertTrue("letters_c" in self.data_wrangler.df.columns)
        self.assertTrue("letters_d" in self.data_wrangler.df.columns)
        self.assertTrue("letters_e" in self.data_wrangler.df.columns)

    def test_calculate_skewness(self):
        # Calculate skewness for the 'numbers' and 'floats' columns
        skewness_values = self.data_wrangler.calculate_skewness()

        # Assuming that the skewness values are calculated correctly, you can add assertions based on the expected skewness
        expected_skewness_numbers = self.df["numbers"].skew().round(1)
        expected_skewness_floats = self.df["floats"].skew().round(1)

        self.assertEqual(skewness_values["numbers"], expected_skewness_numbers)
        self.assertEqual(skewness_values["floats"], expected_skewness_floats)

    def test_get_numeric_columns(self):
        numeric_columns = self.data_wrangler.get_numeric_columns()
        # Add assertions based on the expected numeric columns
        expected_numeric_columns = self.df.select_dtypes(
            include=["float", "int"]
        ).columns
        pd.testing.assert_index_equal(numeric_columns, expected_numeric_columns)

    def test_get_object_columns(self):
        object_columns = self.data_wrangler.get_object_columns()
        # Add assertions based on the expected object columns

    def test_repl_numeric_columns(self):
        self.data_wrangler.repl_numeric_columns()
        # Add assertions based on the expected imputed values


if __name__ == "__main__":
    unittest.main()
