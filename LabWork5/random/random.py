import random

first_list = ["The toy ", "The mouse ", "The laptop ", "The pen ", "The car "]
second_list = ["built ", "created ", "made ", "worked ", "developed "]
third_list = ["in the park", "at home", "in a cafe", "on the beach", "in the shop"]

list_of_strings_list = [first_list, second_list, third_list]

def random_phrase():
    result_string = ""
    for i in range(0,3):
        random_index = random.randrange(0,7)
        result_string = result_string + list_of_strings_list[i][random_index] + ""

    return result_string

print(random_phrase())