# Split data in parts

# import libraries
import numpy as np
import pandas as pd

#load the dataset
data = pd.read_csv("C:\Projects\Federated Learning\Decentralized-FL-Blockchain-Healthcare\data\diabetes.csv")

# randomise the data and make new indexing drop the previous index
data = data.sample(frac =1, random_state=42).reset_index(drop = True)

# divude the data into three hospitals
num_hospitals= 3
split_size = len(data) // num_hospitals
hospital_datasets = []

for i in range(num_hospitals):
    start_idx = i * split_size
    end_idx = (i + 1) * split_size if i < num_hospitals -1 else len(data)
    hospital_data = data.iloc[start_idx:end_idx]
    hospital_datasets.append(hospital_data)
    print(f"Hospital {i+1} has len{hospital_data} rows")

# save the new data in specified location in csv format
for i, hospital_data in enumerate(hospital_datasets):
    hospital_data.to_csv(f'C:\Projects\Federated Learning\Decentralized-FL-Blockchain-Healthcare\data\hospital_{i+1}.csv',index=False)
