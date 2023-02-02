import sys

def pdf_dictionaries(city):
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

    k = " "
    for key, value in capital_cities.items():
        if value == city:
            k = key
            break
    for key, value in states.items():
        if value == k:
            return key
    return "Unknown state\n"
    
    

def chk_arg():
    i = len(sys.argv)
    if i != 2:
        sys.exit(-1)
    

def display_capitals(state):
    print(state)

    
if  __name__ == '__main__':
    chk_arg()
    state = pdf_dictionaries(sys.argv[1])
    display_capitals(state)