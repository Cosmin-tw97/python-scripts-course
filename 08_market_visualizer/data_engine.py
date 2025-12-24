import numpy as np


def generate_market_data(days: int = 100, volatility: float = 0.5) -> Array:
    """
    Generates synthetic market price data using a random walk.
    Demonstrates: NumPy arrays and cumulative sums.
    :param days: number of days to generate. A integer number with default of 100
    :param volatility: volatility parameter
    :return: NumPy arrays of daily returns
    """
    # Starting price
    start_price = 100

    # Generate random daily changes (normally distributed)
    daily_returns = np.random.normal(0, volatility, days)

    # Calculate prices over time (cumulative sum)
    price_trend = start_price + np.cumsum(daily_returns)

    # Generate a list of days for the X axis
    time_axis = np.arange(days)

    return time_axis, price_trend