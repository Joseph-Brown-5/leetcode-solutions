# 1st solution: Time Complexity O(N) Beats: 30.33%
# I'm almost positive there is a way to make this O(1) by using a different data structure

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        count = 1
        x_reversed = ""
        x = str(x)

        for num in x:

            if num != x[len(x) - count]:
                return False

            count += 1
        return True

# 2nd Solution: Time Complexity O(1)? Beats: 71.54%
# this one is better but i don't know why its not higher
# the time complexity changes depending on the variable i believe this is a leetcode thing
# or i don't understand how variable choice would matter


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        return False
        # AAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHH
