import math


def calculate_entropy(password: str) -> float:
    """
    Calculates the Shannon entropy of a password.
    Demonstrates the use of the 'math' module.
    :param password: The password to calculate the entropy of.
    :return: The calculated entropy of. in float format.
    """
    if not password:
        return 0.0

    # Count unique characters
    unique_chars = len(set(password))
    # Possible characters (pool size) - simplified version
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in "!@#$%^&*" for c in password): pool_size += 8

    # Entropy formula: L * log2(Pool)
    if pool_size > 0:
        entropy = len(password) * math.log2(pool_size)
        return round(entropy, 2)
    return 0.0