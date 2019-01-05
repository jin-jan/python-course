#!/usr/local/bin/python3
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0,parent_dir)
from hwk1 import song

def guess_key_value(key, value):
    if type(key) == int:
        return "Invalid key"
    try:
        curr_value = song.dictionary[key.lower()]
        if key.lower() in song.dictionary:
            if type(curr_value) == list:
                return any([i.lower() == value.lower() for i in curr_value])
            if value.lower() == curr_value.lower():
                return True
            else:
                return False
    except KeyError:
        return False
 
print(guess_key_value('artist', 'Imagine Dragons'))
print(guess_key_value('artist', 'Imagine Dragon'))
print(guess_key_value('artis', 'imagine dragons'))
print(guess_key_value('members', 'Benjamin Arthur McKee'))
print(guess_key_value('t','mem3'))
print(guess_key_value(9, 'mem'))

def play_guess():
    result = []
    for attempt in range(5):
        key = input("Try {}: please enter a key: ".format(attempt+1))
        value = input("Try {}: please enter a value: ".format(attempt+1))
        result.append(guess_key_value(key, value))
    print(result)
    print(["Guessed" if i else "Failed" for i in result])
    return all(result)
print(play_guess())

