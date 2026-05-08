import torch
#import jovian
import torch.nn as nn
import pandas as pd
import matplotlib.pyplot as plt
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split

DATA_FILENAME = "carData.csv"
dataframe_raw = pd.read_csv(DATA_FILENAME)
dataframe_raw.head()

your_name = "Johaan Riat"
def customize_dataset(dataframe_raw, rand_str):
    dataframe = dataframe_raw.copy(deep=True)

    #drop rows
    dataframe = dataframe.sample(int(.95*len(dataframe)))
    random_state=int(ord(rand_str[0]))

    #scale input
    dataframe.Year = dataframe.Year * ord(rand_str[1])/100

    #scale target
    dataframe.MSRP = dataframe.MSRP * ord(rand_str[2])/100