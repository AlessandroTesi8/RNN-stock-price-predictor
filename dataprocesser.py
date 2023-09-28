import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os 

def data_process(sequence_length, data_name):
    path= os.getcwd() 
    data=pd.read_csv(path + data_name)
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    scaler = MinMaxScaler()
    sequences, labels = [], []

    for i in range(len(features) - sequence_length):
        scaled_features=scaler.fit_transform(features.iloc[i:i + sequence_length + 1])
        sequence = scaled_features[:sequence_length]
        label = scaled_features[sequence_length,3]  # Lag di un passo
        sequences.append(sequence)
        labels.append(label)

    # Converti sequenze e etichette in array NumPy
    X = np.array(sequences)
    y = np.array(labels)
    return X, y

def last_days(sequence_length, data_name):
    path= os.getcwd() 
    data=pd.read_csv(path +  data_name)
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    features=features.iloc[-( sequence_length + 1) : ]
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    sequences= scaled_features[:-1]
    labels = scaled_features[-1, 3]
    X = np.array(sequences)
    y = np.array(labels)
    max_value = features['Close'].max()  # [:, 3] seleziona la terza colonna
    min_value = features['Close'].min()  # [:, 3] seleziona la terza colonna

    return X, y, max_value, min_value

def tomorrow_pred(sequence_length, data):
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    features=features.iloc[-( sequence_length) : ]
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    sequences= scaled_features[:]
    labels = scaled_features[-1, 3]
    X = np.array(sequences)
    y = np.array(labels)
    max_value = features['Close'].max()  # [:, 3] seleziona la terza colonna
    min_value = features['Close'].min()  # [:, 3] seleziona la terza colonna

    return X, y, max_value, min_value
