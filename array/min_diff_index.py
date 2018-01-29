lst = [5, 3, 2, 4,6,5, 2,4, 4, 5, 7, 7, 2]
m = 2
n= 5


def min_diff(lst, m, n):
    i = 0
    len_lst = len(lst) - 1
    prev = -1
    min_d = len(lst) + 1
    
    d = 0
    for i in range(0, len_lst):
        # First identify the prev index
        if prev == -1:
            if lst[i] == m or lst[i] == n:
                prev = i
        else:
            if lst[i] == m or lst[i] == n:
                if lst[prev] != lst[i]:
                    d = i - prev
                    if min_d > d:
                        min_d = d 
                prev = i
    
    return min_d
