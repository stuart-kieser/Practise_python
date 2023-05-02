def arraySign(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    neg = 0
    for num in nums:
        if num < 0:
            pos += 1
        elif num > 0:
            neg += 1

    if 0 in nums:
        return print(0)
    elif neg % 2 == 0:
        return 1
    elif pos < neg:
        return print(-1)
    else:
        return print(1)


nums = [-1, -2, -3, -4, 3, 2, 1]

arraySign(nums)


# solution
class Solution:
    def arraySign(self, nums):
        if 0 in nums:
            return 0

        res = 1
        for x in nums:
            res *= int(x / abs(x))

        return res
