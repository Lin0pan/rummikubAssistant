
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
    while len(l) > 0:
        a = row(l)
        print(a)
        r = r + [a[-2]]
        l = a[-1]

    for x in r:
        if len(x) < 3:
            l = l + x
            r.remove(x)
    return r, l




def main():
    x = input("bitte Zahlen mit Komma getrennt eingeben eingeben ")
    numberSet = list(x)
    #print(numberSet)
    a = rows(numberSet)
    print ("gelegt: ")
    print(a[-2])
    print ("ueber")
    print(a[-1])

main()
