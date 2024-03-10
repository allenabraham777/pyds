def max_subarray(nums):
    output = 0
    sum = 0
    n = len(nums)
    nums_max = max(nums)
    if nums_max < 0:
        return nums_max
    for i in range(n):
        sum += nums[i]
        if sum < 0:
            sum = 0
        output = max(output, sum)
    return output

