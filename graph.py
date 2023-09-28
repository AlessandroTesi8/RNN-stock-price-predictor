# import required packages
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpdates

def plot_graph(df):
    df = df.reset_index()
    df = df[['Date', 'Open', 'High',
            'Low', 'Close']]
    title = 'Prices For the Period '+ str(df['Date'][0]) + ' to ' + str(df['Date'][len(df['Date'])-1] )
    plt.style.use('dark_background')

    # convert into datetime object
    df['Date'] = pd.to_datetime(df['Date'])
    
    # apply map function
    df['Date'] = df['Date'].map(mpdates.date2num)
    
    # creating Subplots
    fig, ax = plt.subplots()
    
    # plotting the data
    candlestick_ohlc(ax, df.values, width = 0.6,
                    colorup = 'green', colordown = 'red',
                    alpha = 0.8)
    
    # allow grid
    ax.grid(True)
    
    # Setting labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    
    # setting title
    plt.title(title)
    
    # Formatting Date
    date_format = mpdates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    
    fig.tight_layout()
    
    # show the plot
    plt.show()

