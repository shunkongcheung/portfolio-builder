from math import ceil, floor

def get_holdings(budget, sorted_weights, latest_prices):
    '''
    budget: number
    sorted_weights: Array<(symbol: string, weight: number)>
    latest_prices: DataFrame: symbol as index, price as column
    '''
    holdings = []
    original_budget = budget
    for sorted_weight in sorted_weights:
        symbol, weight = sorted_weight

        # calculate purchasable amount
        cur_budget = original_budget * weight
        price = latest_prices[symbol]
        purchasable_amt = floor(cur_budget / price)
        total_spending = purchasable_amt * price

        # deduct purchasable amount from budget
        if budget > total_spending:
            budget = budget - total_spending
        else:
            purchasable_amt = floor(budget / price)
            total_spending = purchasable_amt * price
            budget = budget - total_spending

        # push this into holdings
        if purchasable_amt > 0:
            holdings.append((symbol, purchasable_amt, price,))


    return holdings, budget

