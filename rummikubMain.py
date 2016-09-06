
numberSet = []

#returns row with smallest digit and leftover as tuple
def row(s):
    t=[]
    if len(s) == 0:
        return ([],[])

    s.sort()
    r = [s[0]]

    for i in range(len(s)):
        if s[i] - r[-1] == 1:
            r = r + [s[i]]
    for x in r:
        s.remove(x)

#13-1 problem
    if r[-1] == 13:
        s.sort()
        if len(s)>0 and s[0] == 1:
            r = r + [s[0]]
            s = s[1:]
            for i in range(len(s)):
                if s[i] - r[-1] == 1:
                    r = r + [s[i]]
                    t = t + [s[i]]
    for x in t:
        s.remove(x)
    t=[]

    if r[0] == 1:
        s.sort(reverse=True)
        if len(s)>0 and s[0] == 13:
            r = [13] + r
            t = t + [13]
            for i in range(len(s)):
                if s[i] - r[0] == 1:
                    r = [s[i]] + r
                    t = t + [s[i]]

    for x in t:
        s.remove(x)
    t=[]
    #end 13-1 problem

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
    finalRows([5,6,7,8,9,10,11,12,13,1,2])
    finalRows([1,1,1,2,2,2,13,13,13,3,4,5,6,7,8,5])

main()
