import numpy as np
import pandas as pd


data = pd.read_csv("C:\Projects\Federated Learning\Decentralized-FL-Blockchain-Healthcare\data\diabetes.csv") 

print("Data information\n")
data.info()
print("First 5 rows")
print(data.head())
print("Last 5 rows")
print(data.tail())
print("Number of rows & columns in data")
print(data.shape)
