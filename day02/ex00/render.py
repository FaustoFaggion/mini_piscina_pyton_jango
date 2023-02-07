import sys
import os
import re

def chk_args():
    if len(sys.argv) != 2:
        print("wrong number ofarguments!!")
        sys.exit(-1)
    if sys.argv[1].endswith(".template") == False:
        print("file should have '.template' extension!!")
        sys.exit(-1)
    if not os.path.isfile("./" + sys.argv[1]):
        print("file not found!!")
        sys.exit(-1)
        
def swap_variables():
    dic = globals()
    content = open(sys.argv[1], "r").read()
    for key, value in dic.items():
        sub = "".join(["{", key, "}"])
        content = content.replace(sub, str(value))
    return content

def create_html(content):
    before = "<!DOCTYPE html> \n <html lang=\"en\"> \n <head> \n <meta charset=\"UTF-8\"> \n <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> \n <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> \n <title>Document</title> \n </head> \n <body>"
    after = "\t </body> \n </html>"
    sub = "".join([before, content, after])
    file = sys.argv[1]
    file = file.replace(".template", ".html")
    print(file)
    new_file = open(file, "w")
    new_file.write(sub)
       
if __name__ == "__main__":
    chk_args()
    exec(open("settings.py", "r").read())
    content = swap_variables()
    create_html(content)
