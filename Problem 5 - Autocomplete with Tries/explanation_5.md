### Problem 4 - Autocomplete with Tries

1. Insert (word) method

**Time Complexity:** O(m), where m is the number of characters.

Traverse each character in the word and store in the trie. For each character, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

2. Find method

**Time Complexity:** O(m), where m is the number of characters.

Traverse each character in the word/prefix to check if it's in the trie. For each character, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

3. Suffixes method

**Time Complexity:** O(n x m), where n is number of words and m is the average length of words.

Traverse down the Trie to get all the characters of the words.

**Space Complexity:** O(n x m), where n is number of words and m is the average length of words.

Store all the words in a list.
