import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    my_numbers = json.load(f_obj)
print(my_numbers)

import json

filename = 'username.json'

username = input("What is your name? ")
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
