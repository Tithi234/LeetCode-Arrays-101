class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr List[int]
        :rtype: bool
        """
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            # Check if 2*num or num/2 (if even) already exists
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False








