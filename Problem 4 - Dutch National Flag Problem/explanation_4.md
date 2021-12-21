### Problem 4 - Dutch National Flag Problem

Use quick-sort algorithm. Traverse the list and relocate the number into corresponding buckets. Bucket 1(0) start at the beginning of the array, bucket 2(1) follows bucket 1, bucket 3(2) is at the end of the array.

**Time Complexity:** O(n)

Traverse the list once. And for each element being traversed, the time to put it in the correct bucket is O(1) because we only deal with 3 numbers. Overall, O(n)

**Space Complexity:** O(1)

It's done in place, therefore, O(1)
