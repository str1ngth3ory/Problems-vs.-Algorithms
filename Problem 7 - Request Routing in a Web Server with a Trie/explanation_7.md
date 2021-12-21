1. Insert (parts) method

**Time Complexity:** O(n), where n is the number of path parts.

Traverse through each part of the path and store them in the trie. For each part, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

2. Find method

**Time Complexity:** O(n), where n is the number of path parts.

Traverse each part in the path to check if it's in the trie. For each part, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.
