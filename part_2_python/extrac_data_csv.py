import pandas as pd


def extrac_data_csv():
    """
        Function to read csv file
        Return: Return the data read by the pandas library to the 2017.csv file
    """
    data = pd.read_csv('data_exercise/Archive/2017.csv')
    return data
