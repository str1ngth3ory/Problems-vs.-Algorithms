## TrieNode

1. Constructor

**Time Complexity:** O(1)

**Space Complexity:** O(1)

2. insert (char) method

**Time Complexity:** O(1)

Add an element in a dicitonary, O(1)

**Space Complexity:** O(1)

3. suffixes method

**Time Complexity:** O(n x m), where n is number of words and m is the average length of words.

Traverse down the Trie to get all the characters of the words.

**Space Complexity:** O(n x m), where n is number of words and m is the average length of words.

Store all the words in a list.


## Trie

1. Constructor

**Time Complexity:** O(1)

**Space Complexity:** O(1)

2. insert (word) method

**Time Complexity:** O(m), where m is the number of characters.

Traverse each character in the word and store in the trie. For each character, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

**Space Complexity:** O(1)

3. find method

**Time Complexity:** O(m), where m is the number of characters.

Traverse each character in the word/prefix to check if it's in the trie. For each character, the lookup time for checking if it's already in the trie is O(1) because Trie uses dictionary to store character and TrieNode.

**Space Complexity:** O(1)
