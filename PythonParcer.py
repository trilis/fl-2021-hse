from enum import Enum

class tre():
    empty = 0
    epsilon = 1
    symb = 2
    star = 3
    alt = 4
    concat = 5

class Regexp:
    def __init__(self, type, *args):
        self.type = type
        if (type == tre.symb):
            self.s = args[0]
        elif (type == tre.star):
            self.r = args[0]
        elif (type == tre.alt):
            self.r1 = args[0]
            self.r2 = args[1]
        elif (type == tre.concat):
            self.r1 = args[0]
            self.r2 = args[1]

def nullable(r):
    if (r.type == tre.empty
        or r.type == tre.symb):
        return Regexp(tre.empty)
    elif (r.type == tre.epsilon
        or r.type == tre.star):
        return Regexp(tre.epsilon)
    elif (r.type == tre.concat):
        return Regexp(nullable(r.r1).type & nullable(r.r2).type)
    elif (r.type == tre.alt):
        return Regexp(nullable(r.r1).type | nullable(r.r2).type)

def der(s, r):
    if (r.type == tre.empty
        or r.type == tre.epsilon
        or (r.type == tre.symb and r.s != s)):
        return Regexp(tre.empty)
    elif(r.type == tre.symb):
        return Regexp(tre.epsilon)
    elif(r.type == tre.alt):
        return Regexp(tre.alt, der(s, r.r1), der(s, r.r2))
    elif(r.type == tre.star):
        return Regexp(tre.concat, der(s, r.r), r)
    elif(r.type == tre.concat):
        return Regexp(tre.alt,
            Regexp(tre.concat, der(s, r.r1), r.r2),
            Regexp(tre.concat, nullable(r.r1), der(s, r.r2)))

def derStr(str, r):
    if (str == ''): return r
    else:
        return derStr(str[1:], der(str[0], r))

def match(r, str):
    return nullable(derStr(str, r)).type == tre.epsilon

r = Regexp(tre.concat,
    Regexp(tre.star,
        Regexp(tre.concat,
            Regexp(tre.symb, 'a'), Regexp(tre.symb, 'b'))),
    Regexp(tre.symb, 'a')) #(ab)*a

x = input()
while(x != '0'):
    print(match(r, x))
    x = input()
