
def tostring(arr):
    return "".join(arr)

def permute(arr, l, r):
    if l == r:
        print tostring(arr)
    else:
        for i in range(l, r+1):
            print l, i
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            print l, i
            arr[l], arr[i] = arr[i], arr[l]


string = "ABC"
arr = list(string)
permute(arr, 0, len(arr)-1)

    
