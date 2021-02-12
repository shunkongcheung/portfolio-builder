import pandas as pd

def get_holding_values_dataframe(holdings, latest_prices):
    '''
    holdings: Array<(symbol:string, amount:number, purchase_price: number)>
    latest_prices: DataFrame: symbol as index, price as column
    '''

    # create dataframe from order dict
    dataframe =  pd.DataFrame(holdings, columns=['symbol', 'amount', 'purchase_price'])

    # get current price
    dataframe['current_price'] = dataframe['symbol'].apply(lambda x: latest_prices[x])
    dataframe['price_diff'] = dataframe['current_price'].sub(dataframe['purchase_price'])

    # get current price
    dataframe['spending'] = dataframe['amount'].mul(dataframe['purchase_price'])
    dataframe['ownership'] = dataframe['amount'].mul(dataframe['current_price'])
    dataframe['earning'] = dataframe['ownership'].sub(dataframe['spending'])

    # set symbol as index
    dataframe.set_index('symbol', inplace=True)

    return dataframe, dataframe['earning'].sum()


