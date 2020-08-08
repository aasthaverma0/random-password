
import random
import string


def get_random_alphanumeric_string(len, category):
    print (category)
    category_dict= {'travel': ['River', 'Lake', 'Mountain', 'Desert', 'Waterfall', 'Paris', 'India', 'Canada'],
    'entertainment': ['Cook', 'Bake', 'Swim', 'Fly', 'Movie', 'Netflix', 'Music', 'Eat'],
    'food': ['Pizza', 'Candy', 'Chocolate', 'Taco', 'Ramen', 'Cookie', 'Cake', 'Boba'] }
    if category in category_dict.keys():
        letters_digits = string.ascii_letters + string.digits + '!@#$%&*()_' 
        result_str = ''.join(random.choice(letters_digits) for i in range(len)) 
        print(random.choice(category_dict[category]) + result_str)
        return random.choice(category_dict[category]) + result_str

