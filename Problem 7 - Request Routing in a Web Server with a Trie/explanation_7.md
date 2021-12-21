### RouteTrie

1. Constructor

**Time Complexity:** O(1)

**Space Complexity:** O(1)

2. insert (parts) method

**Time Complexity:** O(n), where n is the number of path parts.

Traverse through each part of the path and store them in the trie. For each part, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

**Space Complexity:** O(1)

3. find method

**Time Complexity:** O(n), where n is the number of path parts.

Traverse each part in the path to check if it's in the trie. For each part, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

**Space Complexity:** O(1)

### RouteTrieNode

1. Constructor

**Time Complexity:** O(1)

**Space Complexity:** O(1)

2. insert method

**Time Complexity:** O(1)

Add an element to a python dictionary, basically a hash map. O(1)

**Space Complexity:** O(1)

### router

1. Constructor

**Time Complexity:** O(1)

**Space Complexity:** O(1)

2. add_handler method

**Time Complexity:** O(n)

Calling the split_path method is O(n) because the split_path method itself is O(n).
RouteTrie.insert() method is O(n).
Overall, it's O(n).

**Space Complexity:** O(n), where n is the number of path parts.

The path_parts variable will cost O(n) space based on the size of the path.
RouteTrie.insert() method cost O(1) space.
Overall, O(n)

3. lookup method

**Time Complexity:** O(n)

Checking empty path is O(1).
Calling the split_path method is O(n) because the split_path method itself is O(n).
Calling TrieRoute.find method is O(n) becasue the find method itself is O(n).
Overall, O(n)

**Space Complexity:** O(n)

The path_parts variable will cost O(n) space based on the size of the path.
RouteTrie.find() method cost O(1) space.
Overall, O(n)

4. split_path method

**Time Complexity:** O(n) - Acoording to https://stackoverflow.com/questions/9068020/running-time-of-string-split-method, string.split() method does two passes through the string - first record the location of separators, second pass the string is split by calling substring repeatedly. Therefore, O(n)

**Space Complexity:** O(n) - the method return a list with size n based on number of path parts.
