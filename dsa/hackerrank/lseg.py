def countWays(nums):
    count = 0
    for i in range(1, len(nums)-1):
        s1 = nums[0:i]
        for j in range(i+1, len(nums)):
            s2 = nums[i:j]
            s3 = nums[j:]
            if(sum(s2) <= sum(s1)+sum(s3)):
                count += 1
    return count % (10**9+7)


print(countWays([1, 2, 3, 4]))
