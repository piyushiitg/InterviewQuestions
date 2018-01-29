

def min_move(target):
    move = None
    n = 0
    sum = 0
    i = 1
    while sum < target:
        print sum , target, n
        sum = sum + i
        n = n + 1
        i = i + 1

    print "Sum", sum, "N", n, "Target", target
    if target == sum:
        return n

    d = sum - target
    if d % 2 == 0:
        return n

    else:
        print d
        sum = sum + n + 1
        print "new Sum", sum
        d = sum - target
        print "---->", d
        if d % 2 == 0:
            return n + 1
        else:
            return n + 2



print min_move(8)
    

    
        

    
