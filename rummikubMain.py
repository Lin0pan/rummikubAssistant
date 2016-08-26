
numberSet = []


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

def placeLeftover(t):
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




def main():
    #x = input("bitte Zahlen mit Komma getrennt eingeben eingeben ")
    #numberSet = list(x)
    numberSet = [1,2,3,4,5,6,7,8,9,10,7,4]
    a = rows(numberSet)
    temp = a
    for x in a[-1]:
        temp = placeLeftover((temp[-2], [x]))

    print(temp)
main()
