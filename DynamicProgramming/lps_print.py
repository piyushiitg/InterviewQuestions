def ispalin(string, a, b):
    while(a<b):
        if(string[a]!=string[b]):
            return 0
        a = a + 1
        b = b - 1 
    return 1

x = []
def printpart(string, out, l, n):
    if l == n:
        print out
        x.append(out)
        return
    for i in range(l, n):
        if ispalin(string, l, i):
            printpart(string, out+"("+string[l:i+1]+")", i+1, n);

 
# Driver program to test above functions
string = "aaaa"
l = 0
m = len(string)
out = ""
printpart(string, out, l,m)
print set(x)
#print "Length is: " + str(longestPalSubstr(string))
