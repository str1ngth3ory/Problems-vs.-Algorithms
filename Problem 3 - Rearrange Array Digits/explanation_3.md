### Problem 3 - Rearrange Array Digits

Utilize Merge Sort to sort the list in descending order. Then alternatingly distribute the digits from largest to smallest into two lists and form the two numbers.

**Time Complexity:** O(nlog(n))

Merge Sort efficiency is O(nlog(n)). Traversing the sorted list is O(n). Therefore, overall time complexity is O(nlog(n)).

**Space Complexity:** O(n)

Merge Sort take O(n) space. The rest of the operations take O(1) - two lists. Overall, O(n).
