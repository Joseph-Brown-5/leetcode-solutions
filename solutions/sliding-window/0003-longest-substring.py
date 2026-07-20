# chat GPT helped me aggressively with this

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}       # character -> last index
        left = 0        # start of current substring
        longest = 0     # longest valid substring length

        for index, character in enumerate(s):
            # Check whether character was already seen
            if character in seen:
                left = max(left, seen[character] + 1)

            seen[character] = index

            current_length = index - left + 1
            longest = max(longest, current_length)
            
            # Possibly move left
            # Update character's latest index
            # Calculate current substring length
            pass

        return longest