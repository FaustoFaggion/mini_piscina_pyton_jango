
def open_file():
    file = open("numbers.txt", 'r')
    return file

def read_content():
    file = open_file()
    content = file.read()
    return content.replace(',', '\n')
    

def print_content():
    content = read_content()
    print(content)

if __name__ == '__main__':
    open_file()
    read_content()
    print_content()
