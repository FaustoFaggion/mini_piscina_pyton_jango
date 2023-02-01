
def myvar():
    
    i = 42
    print(i, " has a type", type(i))
    str1 = "42"
    print(str1, " has a type", type(str1))
    str2 = "quarante-deux"
    print(str2, " has a type", type(str2))
    f = 42.0
    print(f, " has a type", type(f))
    b = True
    print(b, " has a type", type(b))
    l = [42]
    print(l, " has a type", type(l))
    dic = {42 : 42}
    print(dic, " has a type", type(dic))
    t = (42,)
    print(t, " has a type", type(t))
    s = set()
    print(s, " has a type", type(s))

if __name__ == '__main__':
    myvar()