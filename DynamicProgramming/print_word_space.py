
# Python program to print permutations of a given string with
# spaces.
 
# Utility function
def toString(List):
    s = ""
    for x in List:
        if x == '\0':
            break
        s += x
    return s
 
# Function recursively prints the strings having space pattern.
# i and j are indices in 'str[]' and 'buff[]' respectively
def printPatternUtil(string, buff, i, j, n):
    if i == n:
        buff[j] = '\0'
        print toString(buff)
        return
 
    # Either put the character
    buff[j] = string[i]
    printPatternUtil(string, buff, i+1, j+1, n)
 
    # Or put a space followed by next character
    buff[j] = ' '
    buff[j+1] = string[i]
 
    printPatternUtil(string, buff, i+1, j+2, n)
 
# This function creates buf[] to store individual output string
# and uses printPatternUtil() to print all permutations.
def printPattern(string):
    n = len(string)
 
    # Buffer to hold the string containing spaces
    buff = [0] * (2*n) # 2n-1 characters and 1 string terminator
 
    # Copy the first character as it is, since it will be always
    # at first position
    buff[0] = string[0]
 
    printPatternUtil(string, buff, 1, 1, n)
 
# Driver program
string = "ABCD"
printPattern(string)
 
