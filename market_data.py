import random

def get_price_trends():
    # Simulate fetching historical price trends
    price_trends = {
        'wheat': random.uniform(1000, 2000),  # Prices in local currency
        'corn': random.uniform(800, 1500),
        'rice': random.uniform(1500, 2500),
    }
    return price_trends
