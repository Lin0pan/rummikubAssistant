
numberSet = []

#returns row with smallest digit and leftover as tuple
def row(s):

    if len(s) == 0:
        return ([],[])

    s.sort()
    r = [s[0]]

    for i in range(len(s)):
        if s[i] - r[-1] == 1:
            r = r + [s[i]]
    for x in r:
        s.remove(x)
    return r, s

#tries to concatenate leftover to one of the rows
def concatenateLeftover(t):
    r = t[-2]
    l = t[-1]

    ln = []
    rn = []

    for x in t[-2]:
        if len(rows(x + l)[-1]) == 0:
            rn = rn + rows(x + l)[-2]
            l = []
        else:
            rn = rn + [x]
    return rn, l


#returns list of all rows >2 and leftover as tuple
def rows(s):
    l = s
    r = []
    result = []
    while len(l) > 0:
        a = row(l)
        r = r + [a[-2]]
        l = a[-1]

    for x in r:
        if len(x) < 3:
            l = l + x
        else:
            result = result + [x]

    return result, l

#splits rows and insert leftover if possible, returns new list of rows and leftover as tuple
def insertLeftover(t):
    r = t[-2]
    l = t[-1]
    ln = l
    lnn = []
    if len(l) == 0:
        return t

    for x in r:
        for i in range(3, len(x)-1):
            ln = x[i:] + l
            a = rows(ln)

            if len(a[-1]) == 0:
                r.remove(x)
                x = x[:i]
                r = r + [x]
                r = r + a[-2]

                for j in r:
                    if len(j) < 3:
                        lnn = lnn + j
                        r.remove(j)
                return r, lnn
    return t

#def insertLeftoverSeperate(s):

def finalRows(l):
    ##################
    print("eingabe: ")
    print(l)
    ##################

    numberSet = l
    a = rows(numberSet)
    result = a
    ln = []

    for x in a[-1]:
        result = insertLeftover((result[-2], [x]))
        ln = ln + result[-1]

    result = result[-2], ln

    ln = []

    if len(result[-1]) > 0:
        for x in result[-1]:
            result = concatenateLeftover((result[-2], [x]))
            ln = ln + result[-1]

    result = result[-2], ln

    #######################
    print("ergebnis :")
    print(result[-2])
    print("uebrig bleibt: ")
    print(result[-1])
    ########################

def main():
    #x = input("bitte Zahlen mit Komma getrennt eingeben eingeben ")
    #numberSet = list(x)

    finalRows([1,2,3,4,5,3])
    finalRows([1,2,3,2,3,4,3,4,5,4,5,6,5,6,7,6,7,8,7,8,9,10])
    finalRows([1,2,3,4,5,6,7,8,5,6,3,4])
    finalRows([1,2,3,4,5,4,3])
    finalRows([1,2,3,4,5,4,3,4])

main()
