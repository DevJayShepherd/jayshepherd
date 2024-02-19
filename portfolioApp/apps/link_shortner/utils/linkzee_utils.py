import secrets


def generate_secret_key(length: int):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(secrets.choice(chars) for _ in range(length))
