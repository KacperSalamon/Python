#Generator random password in py which we can use in our tests - example in login page of any website.

import random 

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_case = upper_case.lower()

number = "0123456789"

special_characters = "!@#$%^&*_-\/?"

concat = upper_case + lower_case + number + special_characters

len_for_pass >= 10

password = "".join(random.sample(concat, len_for_pass))
