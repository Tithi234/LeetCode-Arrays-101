
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up (strictly increasing)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be first or last element
        if i == 0 or i == n - 1:
            return False

        # Walk down (strictly decreasing)
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # If we reached the end, it’s a valid mountain
        return i == n - 1
