import secrets


def generate_secret_key(length=50):
    # Define the character set for the secret key
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)"

    # Generate a random secret key of the specified length
    return ''.join(secrets.choice(char_set) for _ in range(length))
