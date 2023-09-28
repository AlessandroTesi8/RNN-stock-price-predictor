import pandas as pd
import os 
from graph import plot_graph
import tensorflow as tf
from dataprocesser import tomorrow_pred
from datascraper import last_load
import numpy as np

path= os.getcwd() 
model= tf.keras.models.load_model(path + "/savedRNN.keras")#to change
sequence_length = 365

if __name__=="__main__":
    stock_sigle = input('Scrivi la sigla dello stock da analizzare:\n')
    data = last_load(stock_sigle)
    df = data[-30 :]
    last_days, next_day, M, m= tomorrow_pred(sequence_length, data)
    next_day_pred = model.predict(np.array([last_days]))[0][0]
    print(f'Previsione per domani: {(next_day_pred*(M-m)+m)}, oggi chiude a:{(next_day*(M-m)+m)}')
    plot_graph(df)
