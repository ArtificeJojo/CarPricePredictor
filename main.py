import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from contourpy.util import data


#Read csv file and format data
def LoadData():
    dataTable = pd.read_csv('carData.csv')
    dataTable = dataTable.iloc[:]
    headers = ["Brand", "Name", "Year", "Market Price", "Current Price", "Miles",
               "Body Style", "Engine", "Fuel", "Transmission", "Owners", "Damage", ""]
    dataTable.columns = headers

    isMissing = dataTable
    isMissing.isna().any()
    isMissing.isnull().any()

    return dataTable

def PriceToInt(data):
    data['Market Price'] = data['Market Price'].astype(int)
    return data

def main():
    data = LoadData()

    data = PriceToInt(data)

    print(data.head())

main()