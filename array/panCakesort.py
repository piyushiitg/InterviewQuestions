
# reverse the array from o to i
def flip(arr, i):
    j = 0 
    while j<i:
        arr[j], arr[i] = arr[i], arr[j]
        j = j+1
        i = i - 1

def max_index(arr, current_size):
    i = 0
    mi = 0
    while i<current_size:
        if arr[i] > arr[mi]:
            mi = i
        i = i + 1
    return mi

def pancake(arr):
    current_size = len(arr)
    while current_size > 0:
        mi = max_index(arr, current_size)
        if mi != current_size - 1:
            flip(arr, mi)
            flip(arr, current_size-1)
        current_size -= 1     

nums = [3, 2]
pancake(nums)
print nums
