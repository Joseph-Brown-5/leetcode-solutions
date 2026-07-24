# first try Beats %11.08

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        smallest = nums[0]
        largest = nums[len(nums) - 1]
        denom = 1
        result = 1

        while denom <= smallest:
            if smallest % denom == 0 and largest % denom == 0:
                result = denom
            denom += 1

        return result

    # second try uses fancy math

    class Solution(object):

    def findGCD(self, nums):
        large = max(nums)
        small = min(nums)
        while small != 0:
            large, small = small, large % small
        return large


# ahhhhhhhhhhhhhhh
