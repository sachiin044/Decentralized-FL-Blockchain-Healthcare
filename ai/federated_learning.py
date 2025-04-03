import tensorflow as tf
import tensorflow_federated as tff
import numpy as np
import pandas as pd
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


# load prepare the data for the TFF converting data in float32 for tensorflow
# and processing data in batches return the data in tenosrflow dataset
def create_tf_dataset(hospital_data):
    features = hospital_data.drop("Outcome", axis=1).values.astype('float32')
    labels = hospital_data['Outcome'].values.astype('float32')
    return tf.data.Dataset.from_tensor_slices(
        (features, labels)
    ).batch(32)

# load the hospital_data
hospital_data = [
    create_tf_dataset(pd.read_csv(f'C:\Projects\Federated Learning\Decentralized-FL-Blockchain-Healthcare\data\hospital_{i+1}.csv'))
    for i in range(3)
]

# 

print("\nCode runs perfectly")




