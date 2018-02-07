def kadane_algo(a):
    low = high = i = j = 0
    s = 0
    max_sum = min(a) - 1
    for i in range(len(a)):
        s =  s + a[i]
        print s, max_sum
        if s > max_sum:
            max_sum = s
            low = j
            high = i
            print "------", max_sum, low, high
        elif s < 0:
            j = i + 1
            s = 0
    return max_sum, low, high


a = [2, -3, 4, 5, -1, 11]
print a
print kadane_algo(a)

