import pandas as pd
import numpy as np
from scipy.stats import boxcox

class DataFrameTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def identify_skewed_columns(self, threshold=1.0):
        skewed_cols = self.dataframe.apply(lambda x: x.skew()).sort_values(ascending=False)
        return skewed_cols[abs(skewed_cols) > threshold].index.tolist()

    def transform_skewed_columns(self, columns):
        for column in columns:
            if self.dataframe[column].min() <= 0:
                self.dataframe[column] += 1 - self.dataframe[column].min()
            self.dataframe[column], _ = boxcox(self.dataframe[column])

    def identify_outliers(self, threshold=1.5):
        outliers = {}
        for column in self.dataframe.select_dtypes(include=[np.number]).columns:
            Q1 = self.dataframe[column].quantile(0.25)
            Q3 = self.dataframe[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            outliers[column] = self.dataframe[(self.dataframe[column] < lower_bound) | (self.dataframe[column] > upper_bound)].index.tolist()
        return outliers

    def remove_outliers(self, outliers):
        for column, indices in outliers.items():
            self.dataframe = self.dataframe.drop(indices)

    def compute_correlation_matrix(self):
        numeric_df = self.dataframe.select_dtypes(include=[np.number])
        return numeric_df.corr()

    def drop_highly_correlated_columns(self, threshold=0.85):
        corr_matrix = self.compute_correlation_matrix()
        upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        to_drop = [column for column in upper_tri.columns if any(upper_tri[column].abs() > threshold)]
        self.dataframe.drop(columns=to_drop, inplace=True)
        return to_drop
