import sys

def pdf_dictionaries(list):
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
    for i in range(len(list)):
        found = False
        for key, value in states.items():
            state = str(list[i].title())
            if  " ".join(state.split()) == key:
                for k, val in capital_cities.items():
                    if k == value:
                        found = True
                        print(val + " is the capital of " +  key)

        for key_, value_ in capital_cities.items():
            capital = str(list[i].title())
            if " ".join(state.split()) == value_:
                for k, val in states.items():
                    if val == key_:
                        found = True
                        print(value_ + " is the capital of " +  k)
        if found == False:
            if list[i] != '':
                print(list[i], "is nether a capital city nor a state")

                        
def chk_arg():
    i = len(sys.argv)
    if i != 2:
        sys.exit(-1)
 
def parse_arg():
    s = str(sys.argv[1])
    list = s.split(',')
    for i in range(len(list)):
        list[i] = list[i].strip()
    return list

if  __name__ == '__main__':
    chk_arg()
    list = parse_arg()
    pdf_dictionaries(list)
