import sys

def pdf_dictionaries(state):

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    val = " "
    for key, value in states.items():
        if key == state:
            val = value
            break
    for key, value in capital_cities.items():
        if key == val:
            return value
    return "Unknown state\n"
    
    

def chk_arg():
    i = len(sys.argv)
    if i != 2:
        sys.exit(-1)
    

def display_capital(city):
    print(city)

    
if  __name__ == '__main__':
    chk_arg()
    city = pdf_dictionaries(sys.argv[1])
    display_capital(city)