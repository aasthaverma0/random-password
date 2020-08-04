
import random
import string

def get_random_alphanumeric_string(len):
    letters_digits_symbols = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters_digits_symbols) for i in range(len))
    travel_list = ['river', 'lake', 'mountain', 'desert', 'waterfall', 'paris', 'india', 'alaska', 'canada', 'sydney', 'egypt']
    entertainment_list = ['cook', 'bake', 'swim', 'fly', 'movie', 'netflix', 'music', 'theater', 'run', 'walk']
    food_list = ['pizza', 'candy', 'chocolate', 'taco', 'noodle', 'sugar', 'ramen', 'gummy', 'cookie', 'cake', 'boba']
    print("Random password is " + random.choice(travel_list) + result_str)
    return "Random password is " + random.choice(travel_list) + result_str
    print("Random password is " + random.choice(entertainment_list) + result_str)
    return "Random password is " + random.choice(entertainment_list) + result_str
    print("Random password is " + random.choice(food_list) + result_str)
    return "Random password is " + random.choice(food_list) + result_str

get_random_alphanumeric_string(6)
get_random_alphanumeric_string(6)
get_random_alphanumeric_string(6)
