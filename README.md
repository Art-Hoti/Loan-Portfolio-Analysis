Loan Portfolio Analysis

Table of Contents

Description
Installation Instructions
Usage Instructions
File Structure
Licence Information
Description

The Loan Portfolio Analysis project aims to perform exploratory data analysis (EDA) on a large financial institution’s loan portfolio. By analysing loan data, the project seeks to uncover patterns, relationships, and anomalies that will inform decisions regarding loan approvals, pricing, and risk management. The ultimate goal is to enhance the performance and profitability of the loan portfolio.

Key aspects of the project include:

Data Extraction: Extracting loan data from a cloud database.
Data Loading: Loading data into a Pandas DataFrame for analysis.
Data Cleaning: Handling missing values and transforming skewed data.
Outlier Removal: Identifying and removing outliers from the dataset.
Correlation Analysis: Dropping highly correlated columns to avoid multicollinearity.
Data Visualisation: Using visualisations to identify patterns and relationships.
Installation Instructions

1. Clone the Repository:
git clone https://github.com/Art-Hoti/Loan-Portfolio-Analysis-1.git

2. Navigate to the Project Directory:
cd Loan-Portfolio-Analysis-1

3. Install Dependencies:
pip install -r requirements.txt

Usage Instructions

1. Run the Data Extraction Script:
python data_extraction.py

2. Perform EDA using Jupyter Notebooks:
jupyter notebook

File Structure
Loan-Portfolio-Analysis-1/
│
├── data_extraction.py       # Script to extract data from AWS RDS
├── dataframe_transform.py   # Contains DataFrameTransform class for EDA transformations
├── plotter.py               # Contains Plotter class for data visualisations
├── requirements.txt         # Required Python packages
├── README.md                # Project documentation
├── notebooks/               # Jupyter notebooks for EDA
│   └── eda.ipynb            # Main notebook for exploratory data analysis
└── data/                    # Directory to store data files
    └── loans_data.csv       # Extracted loan data

Licence Information

This project is licensed under the MIT Licence. See the LICENSE file for details.

