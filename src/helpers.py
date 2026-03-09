import random
import string


def rand_str(n: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(n))


def generate_user() -> dict:
    return {
        "email": f"eva_{rand_str(8).lower()}@yandex.ru",
        "password": rand_str(12),
        "name": f"Eva_{rand_str(6)}",
    }