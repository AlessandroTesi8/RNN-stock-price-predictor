import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import os 
from dataprocesser import data_process, last_days

sequence_length = 365
X, y = data_process(sequence_length, 'datasets/amazon.csv')

# Dividi i dati in set di addestramento e test
split_ratio = 0.95
split_index = int(split_ratio * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

stock_list=['apple.csv', 'google.csv', 'microsoft.csv', 'tesla.csv']
for stock in stock_list:
    X, y = data_process(sequence_length, 'datasets/'+stock)
    split_index = int(split_ratio * len(X))
    X_train, X_test = np.concatenate((X_train, X[:split_index]), axis=0), np.concatenate((X_test, X[split_index:]), axis=0)
    y_train, y_test = np.concatenate((y_train, y[:split_index]), axis=0), np.concatenate((y_test, y[split_index:]), axis=0)

print(X_train.shape, X_test.shape)

# Crea il modello LSTM complesso
model = Sequential()
model.add(LSTM(100, return_sequences=True, activation='relu', input_shape=(sequence_length, 5)))
model.add(Dropout(0.2))
model.add(LSTM(100, return_sequences=True, activation='relu'))
model.add(Dropout(0.2))
model.add(LSTM(100, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Addestra il modello
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)# rimettere epochs poi
# Valuta il modello
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Esegui una previsione per il 31° giorno
last_days, next_day, M, m= last_days(sequence_length, 'datasets/amazon.csv')
next_day_pred = model.predict(np.array([last_days]))[0][0]

print(f'Previsione per il {sequence_length}° giorno: {(next_day_pred*(M-m)+m)}, vero {sequence_length}° giorno:{(next_day*(M-m)+m)}')
# Salva il modello in formato SavedModel
model.save(os.getcwd() + "/RNN stock prices/savedRNN.keras")
