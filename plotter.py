import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # Import NumPy

class Plotter:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def plot_histogram(self, columns):
        self.dataframe[columns].hist(bins=50, figsize=(20, 15))
        plt.show()

    def plot_box(self, columns):
        self.dataframe[columns].plot(kind='box', subplots=True, layout=(int(len(columns)/3)+1, 3), figsize=(20, 15))
        plt.show()

    def plot_correlation_matrix(self):
        numeric_df = self.dataframe.select_dtypes(include=[np.number])
        corr = numeric_df.corr()
        plt.figure(figsize=(20, 15))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
        plt.show()
