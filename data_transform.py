import pandas as pd

class DataTransform:
    def __init__(self, df):
        self.df = df

    def convert_to_datetime(self, column_name, date_format=None):
        self.df[column_name] = pd.to_datetime(self.df[column_name], format=date_format, errors='coerce')
        return self.df

    def convert_to_numeric(self, column_name):
        self.df[column_name] = pd.to_numeric(self.df[column_name], errors='coerce')
        return self.df

    def convert_to_categorical(self, column_name):
        self.df[column_name] = self.df[column_name].astype('category')
        return self.df

    def remove_symbols(self, column_name, symbols):
        for symbol in symbols:
            self.df[column_name] = self.df[column_name].str.replace(symbol, '')
        return self.df
