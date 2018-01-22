
def lcs(X, Y, m, n):
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0

            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]               

def lcs_recursion(X, Y, m, n):
    if (m == 0 or n == 0):
        return 0
    if (X[m-1] == Y[n-1]):
        return 1 + lcs_recursion(X, Y, m-1, n-1) 
    return max(lcs_recursion(X, Y, m, n-1), lcs_recursion(X, Y, m-1, n))

def lcs_print(m , n):
    index = L[m][n]
    plcs = [""]*(index+1)
    plcs[index] = "\0"
    i = m
    j = n
    while ( i > 0 and j > 0):
        if X[i-1] == Y[j-1]:
            plcs[index-1] = X[i-1]
            i = i - 1
            j = j - 1
            index = index - 1
        elif L[i-1][j] > L[i-1][j-1]:
            i = i - 1
        else:
            j = j - 1
    return plcs
            

          
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
L = [[0]*(m+10) for i in xrange(n+10)]
print "Length of LCS is ", lcs_recursion(X, Y, m, n)
print "Length of LCS is ", lcs(X, Y, m, n)
print lcs_print(m, n)
print L
