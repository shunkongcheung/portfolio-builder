from pypfopt.discrete_allocation import get_latest_prices

from get_holdings import get_holdings
from get_holding_values_dataframe import get_holding_values_dataframe
from get_prices_dataframe import get_prices_dataframe
from get_sorted_weights import get_sorted_weights
from get_symbols import get_symbols


def calculate_earning():
    est_from_date, est_to_date = '2005-01-01', '2020-12-30'
    symbols = get_symbols()
    prices = get_prices_dataframe(symbols, est_from_date, est_to_date)

    sorted_weights = get_sorted_weights(prices)
    latest_prices = get_latest_prices(prices)

    BUDGET = 5000
    holdings, remains = get_holdings(BUDGET, sorted_weights, latest_prices)
    spending = BUDGET - remains

    # calculate holdings return in x years
    realize_from_date, realize_to_date = '2021-02-01', '2021-02-11'
    realized_prices = get_prices_dataframe(symbols, realize_from_date, realize_to_date)
    realized_latest_prices = get_latest_prices(realized_prices)
    dataframe, earning = get_holding_values_dataframe(holdings, realized_latest_prices)

    print (f'Estimate: {est_from_date} {est_to_date}, Realized: {realize_to_date}')
    print (dataframe)
    print( earning)

if __name__ == '__main__':
    calculate_earning()
