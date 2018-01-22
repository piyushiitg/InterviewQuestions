"""
longest Plaindrome Subsequence and substring
"""


def lps_recursion(x, i, j):
    if i < 0 or j < 0:
        return 0
    if i== j:
        return 1

    if (x[i] == x[j] and i+1 == j):
        return 2
    if x[i] == x[j]:
        return lps_recursion(x, i+1, j-1) + 2
    return max(lps_recursion(x, i, j-1), lps_recursion(x, i+1, j))
    
def lps1(x, n, L):
    for i in range(n):
        L[i][i] = 1

    for k in range(2, n+1):
        for i in range(1, n-k+1):
            j = i+k-1
            if x[i] == x[j] and k == 2:
                L[i][j] = 2

            elif x[i] == x[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])
    return L[0][n-1]
    
def lps(str):
    n = len(str)
 
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
    x = [["" for x in range(n)] for x in range(n)]
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
        x[i][i] = str[i:i+1] 
        print str[i:i+1]
 
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
                print str[i:j+1]
                x[i][j] = str[i:j+1]
            elif str[i] == str[j]:
                # 1 3 abb
                # a aba ba
                # x[i] [0, 'a', 0, 0, 0, 0]
                L[i][j] = L[i+1][j-1] + 2
                x[i][j] = str[i:i+1] + x[i+1][j-1] + str[j:j+1]
                #x[i][j] = x[i:i+1] + x[i+1:j-1] + x[j-1:j]
                #print x[i][j]
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
                #L[i][j] = 1

    print x
    return L[0][n-1]

x = "ababa"
print x
n = len(x)
L = [[0]*(n+1)]*(n+1)
#print lps_recursion(x, 0, n-1)
#print lps1(x, n, L)
print lps(x)
