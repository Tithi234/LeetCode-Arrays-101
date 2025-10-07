class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Create two lists for even and odd numbers
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]

        # Combine them: evens first, then odds
        return evens + odds
