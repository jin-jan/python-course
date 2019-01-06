#!/usr/local/bin/python3
import os

def write_save_file(file_name):
    open_close_file(file_name, 'w')

def append_text(file_name):
    open_close_file(file_name, 'a')

def open_close_file(file_name, mode):
    note_file = open(file_name, mode)
    save_text = input("Please enter your text: ")
    note_file.write(save_text)
    note_file.write("\n")
    note_file.close()

def write_new_file():
    file_name = input("Please enter file name: ")
    write_save_file(file_name)

def read_file(file_name, out_p=False):
    lines = []
    note_file = open(file_name, 'r')
    for line in note_file:
        if out_p:
            print(line, end="")
        lines.append(line)
    note_file.close()
    return lines
    
def delete_file(file_name):
    os.remove(file_name)

def replace_line(file_name):
    try:
        line_num = input("Please provide the line number to be update: ")
        int_line_num = int(line_num)
    except ValueError as e:
        print("Invalid line number: {}".format(e))
        return
    text_replace = input("Please provide the new text: ")
    lines = read_file(file_name)
    new_text = []
    if int_line_num > len(lines):
        print("Invalid line number")
        return 
    elif int_line_num <= 0:
        print("Invalid line number")
        return
    else:
        for line in range(len(lines)):
            if line == (int_line_num-1):
                new_text = lines[:line]
                new_text.append(text_replace + "\n")
                new_text = new_text + lines[line+1:] 
        note_file = open(file_name, 'w')
        for line in new_text:
            note_file.write(line)
        note_file.close()

def main():
    quit = False
    while(not quit):
        try:
            file_name = input("Welcome, please enter the file name: ")
            note_file = open(file_name, 'r')
            note_file.close()
            ask_action = input("What do you want to do? [read/delete/append/replace/quit]: ")
            if ask_action == 'read':
                read_file(file_name, True)
            elif ask_action == 'delete':
                delete_file(file_name)
                write_new_file()
                continue
            elif ask_action == 'append':
                append_text(file_name)
                continue
            elif ask_action == 'replace':
                replace_line(file_name)
                continue
            elif ask_action == 'quit':
                quit = True
            else:
                print("Try again")
        except IOError:
            write_save_file(file_name)

main()
