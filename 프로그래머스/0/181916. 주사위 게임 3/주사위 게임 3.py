def solution(a, b, c, d):
    nums = [a,b,c,d]
    count = [nums.count(i) for i in nums]
    
    if max(count) ==4:
        return 1111*a
    elif max(count) == 3:
        p = nums[count.index(3)]
        q = nums[count.index(1)]
        return (10*p + q)**2
    elif max(count) == 2:
        if min(count) == 2:
            return (a+b)*abs(a-b) if a!=b else (a+c)*abs(a-c)
        else:
            p = nums[count.index(2)]
            return (a*b*c*d) / p**2
    else:
        return min(nums)