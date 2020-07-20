
import random
import string

def get_random_alphanumeric_string(length):
    letters_digits_symbols = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters_digits_symbols) for i in range(length))
    print("Random password is", "name" + result_str)

get_random_alphanumeric_string(6)
get_random_alphanumeric_string(6)