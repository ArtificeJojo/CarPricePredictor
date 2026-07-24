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

def Normalize(data):
    data['Market Price'] = data['Market Price']/data['Market Price'].max()
    data['Current Price'] = data['Current Price'] / data['Current Price'].max()
    data['Miles'] = data['Miles'] / data['Miles'].max()

    bins = np.linspace(data['Market Price'].min(), data['Market Price'].max(), 4)
    groupNames = ['Low', 'Medium', 'High']
    data['Binned Price'] = pd.cut(data['Current Price'], bins, labels=groupNames, include_lowest=True)

    return data

def ToNum(data):
    pd.get_dummies(data['Brand'])
    pd.get_dummies(data['Name'])
    pd.get_dummies(data['Body Style'])
    pd.get_dummies(data['Engine'])
    pd.get_dummies(data['Fuel'])
    pd.get_dummies(data['Transmission'])

    data.describe()

    return data


def main():
    data = LoadData()
    data = PriceToInt(data)
    data = Normalize(data)
    data = ToNum(data)

    print(data)

main()