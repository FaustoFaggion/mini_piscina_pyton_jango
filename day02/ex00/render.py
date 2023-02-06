import sys
import os
import re

def open_file():
    file = open("settings.py", "r")
    return file

def read_content(file):
    content = file.read()
    return content

def make_dictionary(content: str):
    dic = {}
    list = content.split()
    
    for item in list:
        item.split("=")
        
        
if __name__ == "__main__":
    file = open_file()
    content = read_content(file)
    dic = make_dictionary(content)