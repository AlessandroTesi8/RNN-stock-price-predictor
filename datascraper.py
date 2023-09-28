import yfinance as yf
from datetime import datetime, timedelta
import os 

#df = yf.download('AMZN', start='2020-01-01')

#plot_graph(df)
path= os.getcwd() + "/datasets/last_load.csv"
#df.to_csv(path, index=True)  # index=False per evitare di salvare l'indice del DataFrame come colonna separatatesla

def last_load(stock_name):
    load_date = datetime.today() - timedelta(days=666)
    load_date_str = load_date.strftime('%Y-%m-%d')
    df = yf.download(stock_name, start=load_date_str)
    #df.to_csv(path, index=True)
    return df
