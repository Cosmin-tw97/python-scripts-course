def celsius_to_fahrenheit(c: float) -> float:
    """
    Converts temperature from Celsius to Fahrenheit.
    :param c: The temperature in Celsius.
    :return: A float representing the temperature in Fahrenheit.
    """
    return round((c * 9/5) + 32, 2)

def km_to_miles(km: float) -> float:
    """
    Converts distance from km to miles.
    :param km: The distance in kilometers.
    :return: A float representing the distance in miles.
    """
    return round(km * 0.621371, 2)