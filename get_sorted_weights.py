from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import expected_returns, risk_models

import numpy as np

def get_sorted_weights(prices):
    '''
    prices: dataframe of the following shape. Column as symbols, Date as indices
                      AAL       AAPL    GOOGL
      Date
      2014-02-14  32.439728   17.411098  0.00
      2014-02-15  32.439728   17.411098  0.00
    '''
    # calculate parameters
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)

    # remove infinite values
    symbols = prices.columns
    for symbol in symbols:
        # if value is infinite
        mu_value = mu[symbol]
        if not np.isfinite(mu_value) or mu_value == 0:
            # delete from means
            del mu[symbol]

            # delete from sample covariance
            S.drop(symbol, axis=1, inplace=True)
            S.drop(symbol, axis=0, inplace=True)

    # calculate efficient frontier
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    sorted_weights = sorted(cleaned_weights.items(), key=lambda x: -x[1])
    return sorted_weights

