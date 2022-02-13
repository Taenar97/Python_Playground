from __future__ import print_function
import os
import pandas as pd
data_path = ['C:\\Users\\User\\Dropbox\\Machine Learning\\Intel-ML101_Class1\\data\\Iris_Data.csv']
print (data_path)
data = pd.read_csv(data_path)
#print(data.iloc[:5])