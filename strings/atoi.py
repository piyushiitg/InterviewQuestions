

def atoi(num):
    res = 0
    for i in range(len(num)):
        res = res*10 + (ord(num[i]) - ord('0'))

    return res

def atof(num):
    res = 0
    a, b = num.split(".")
    for i in range(len(a)):
        res = res*10 + (ord(num[i]) - ord('0'))

    print res, b, len(b)
    res2 = 0
    count = 1
    for i in range(len(b)):
        print "----->", (ord(b[i]) - ord('0')) * pow(10, -count)
        res2 = res2 + (ord(b[i]) - ord('0')) * pow(10, -count)
        print res2
        count = count + 1
    return res + res2

a = "89821"
print atoi(a)
a = "89.321"
print atof(a)
