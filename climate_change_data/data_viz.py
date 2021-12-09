#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#load data
climate_data = pd.read_csv("/data/Temperature_change_Data.csv")
#view data
print(climate_data.head())