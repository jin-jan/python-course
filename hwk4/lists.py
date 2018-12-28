import random
global my_unique_list
global my_left_overs
my_left_overs = [] 
my_unique_list = []

def add_item_list(item):
    if item not in my_unique_list:
        my_unique_list.append(item)
        return True
    else:
        my_left_overs.append(item)
        return False

print("Adding items to my_unique_list")
for i in "my dog's name is dog , today is monday 9 , i like monday , my favorite number is 9".split():
    add_item_list(i)
for i in [False, False, True, False, True, True]:
    add_item_list(i)
for i in range(0,10):
    add_item_list(random.randint(0,5))
print("my_left_overs list: \n{}\n".format(my_left_overs))
print("my_unique_list: \n{}\n".format(my_unique_list))
