### Problem 1 - Square Root of an Integer

To find the square root of an integer, n, we are essentially reducing the difference of a and b where a * b = n. Start with a = 1, keep doubling a and reducing b by half until b is about to exceed a, the square root of n must lie between the current a and b. Then we can traverse between a and a + (b-a)/2 to find the square root.

**Time Complexity:** O(log(n))

We keep reducing the amount numbers to be traversed by 2 each time we multiply a by 2 and divide b by 2. Therefore, the time complexity is O(log(n)).

**Space Complexity:** O(1)

Need two variables to store dynamic a and b values.
