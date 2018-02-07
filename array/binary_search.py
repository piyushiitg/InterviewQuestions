


def binary_search(a, num):
    low = 0 
    high = len(a)
    while(low < high):
        mid = (low+high)/2
        if a[mid] == num:
            return mid

        if num > a[mid]:
            low = mid + 1

        elif num < a[mid]:
            high = high - 1

    return -1

def find_pivot(arr, low, high):
    if high < low:
        return -1

    if high == low:
        return low
        
    mid = (low+high)/2
    if mid < high and arr[mid] > arr[mid+1]:
        return mid

    if mid > low and arr[mid] < arr[mid-1]:
        return mid 

    

    

def binary_search_rotate(a, num):
    low = 0 
    high = len(a)
    while(low < high):
        mid = (low+high)/2
        
        if a[mid] == num:
            return num

        if a[mid-1] < a[mid] and a[mid+1] > a[mid]:
            if num < a[mid]:
                high = mid - 1
            

        elif num < a[mid]:
            high = high - 1

    return -1





a = range(6, 10, 1) + range(1, 6, 1)
print a
print binary_search(a, 6)
