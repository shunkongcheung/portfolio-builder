import yfinance as yf  
import pandas as pd
from datetime import datetime, timedelta

def get_prices_dataframe(symbols, from_date=None, to_date=None):
    '''
    symbol: Array of string, e.g. ['APPL', 'GOOGL']
    from_date: string of date in format of YYYY-MM-DD
    to_date: string of date in format of YYYY-MM-DD

    retrieve prices from yahoo finance
    '''
    if not to_date:
        to_date = datetime.now()
        to_date = to_date.strftime("%Y-%m-%d")

    if not from_date:
        from_date = datetime.now()
        from_date = from_date - timedelta(days=365*7)
        from_date = from_date.strftime("%Y-%m-%d")

    data = yf.download(symbols,from_date,to_date)
    dataframe =  pd.DataFrame(data['Adj Close'])
    return dataframe

