class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Initialize the maximum element to the right as -1
        max_right = -1

        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Store current value temporarily
            current = arr[i]
            # Replace current with the max element seen so far
            arr[i] = max_right
            # Update max_right if current is greater
            max_right = max(max_right, current)

        return arr
