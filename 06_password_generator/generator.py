import secrets
import string

def generate_secure_password(length: int = 16) -> str:
    """
    Generates a cryptographically secure random password.
    Uses 'secrets' module for better security than 'random'.
    :param length: Length of the password to generate. A integer with default of 16 characters.
    :return: Secure password.
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    # Generate password choosing random characters from the pool
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password