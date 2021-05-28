import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    generated_id = []
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    for _ in range(number_of_small_letters):
        generated_id.append(lowercase_letters[random.randint(0, len(lowercase_letters) - 1)])
    for _ in range(number_of_capital_letters):
        generated_id.append(uppercase_letters[random.randint(0, len(uppercase_letters) - 1)])
    for _ in range(number_of_digits):
        generated_id.append(digits[random.randint(0, len(digits) - 1)])
    for _ in range(number_of_special_chars):
        generated_id.append(allowed_special_chars[random.randint(0, len(allowed_special_chars) - 1)])

    random.shuffle(generated_id)

    return "".join(generated_id)
