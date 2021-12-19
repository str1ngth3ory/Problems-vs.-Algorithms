### Problem 1 - Search in a Rotated Sorted Array

In each recursion, find which half of the subarray the number is, and traverse through only one side - basically a binary search.

**Time Complexity:** O(log(n))

We keep reducing the amount numbers to be traversed by 2 each time. Therefore, the time complexity is O(log(n)).

**Space Complexity:** O(0)

Operation was done on the original array.
