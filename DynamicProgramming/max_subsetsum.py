
def is_subsetsum(sum_set, n, total):
    if n < 0:
        return False
    if n == 0 and total > 0:
        return False
    if total == 0:
        return True
    
    if (sum_set[n-1] > sum):
        return is_subsetsum(sum_set, n-1, total)

    x = is_subsetsum(sum_set, n-1, total - sum_set[n-1]) 

    if x == True:
        return True

    y = is_subsetsum(sum_set, n-1, total)

    if y == True:
        return True
    return False


def subset_sum(sum_set, n total):
         
sum_set = [3, 34, 5, 4, 1, 11, 12]
total = 11

n = len(sum_set) 
s = [0]*(n+1)

print is_subsetsum(sum_set, n, total)
