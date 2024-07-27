import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file {file_path} could not be parsed.")
        return None

file_path = 'loan_data.csv'

loan_data = load_data(file_path)

if loan_data is not None:
    print("Shape of the data:", loan_data.shape)
    
    print("Sample of the data:")
    print(loan_data.head())
    
    print("Column names:")
    print(loan_data.columns)
else:
    print("Data loading failed.")
