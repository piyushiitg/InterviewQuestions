

def next_greater_number(num):
    num = str(num)
    nums = ",".join(num).split(",")
    map(int, nums)
    j = len(nums) - 1
    i = j - 1
    while nums[i] > nums[j] and i > 0:
        j = j - 1
        i = i - 1

    rest = nums[j:] 
    map(int, rest) 
    rest.sort()
    print ""
    print "----", rest, num[i]     
    for m, k in enumerate(rest):
        if rest[m] > nums[i]:
           rest[m], nums[i] = nums[i], rest[m]
           break

    new_number = nums[: j] + rest
    
    return "".join(new_number)
   

num = 45123
print "input ", num
print "output", next_greater_number(num)
