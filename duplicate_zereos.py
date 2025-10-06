class Solution(object):
def duplicateZeros(self, arr):
"""
:type arr: List[int]
:rtype: None Do not return anything, modify arr in-place instead.
"""
n = len(arr)
zeros = arr.count(0)

```
    # Traverse from the end so we don't overwrite unprocessed elements
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            zeros -= 1
            # place duplicated zero if it fits within array bounds
            if i + zeros + 1 < n:
                arr[i + zeros + 1] = 0
        # shift the element right by 'zeros' positions if within bounds
        if i + zeros < n:
            arr[i + zeros] = arr[i]
```

if **name** == "**main**":
tests = [
[1,0,2,3,0,4,5,0],
[1,2,3],
[0,0,0,0,0]
]
for original in tests:
arr = list(original)        # work on a copy to show input vs output
Solution().duplicateZeros(arr)
print("input :", original)
print("output:", arr)
print("-" * 30)


