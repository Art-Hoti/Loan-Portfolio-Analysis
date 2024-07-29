import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        return self.df.dtypes

    def extract_statistics(self):
        stats = {
            'mean': self.df.mean(numeric_only=True),
            'median': self.df.median(numeric_only=True),
            'std_dev': self.df.std(numeric_only=True)
        }
        return pd.DataFrame(stats)

    def count_distinct_values(self):
        distinct_counts = {col: self.df[col].nunique() for col in self.df.select_dtypes(include=['category']).columns}
        return pd.Series(distinct_counts)

    def dataframe_shape(self):
        return self.df.shape

    def null_value_counts(self):
        null_counts = self.df.isnull().sum()
        null_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        null_info = pd.DataFrame({
            'null_count': null_counts,
            'null_percentage': null_percentage
        })
        return null_info

    def summary_statistics(self):
        return self.df.describe(include='all')

    def get_column_unique_values(self, column_name):
        if column_name in self.df.columns:
            return self.df[column_name].unique()
        else:
            return f"Column '{column_name}' does not exist in the DataFrame."

    def get_column_value_counts(self, column_name):
        if column_name in self.df.columns:
            return self.df[column_name].value_counts()
        else:
            return f"Column '{column_name}' does not exist in the DataFrame."
