Problem 5:
Trie Auto complete problem uses class Trie and TrieNode for suggesting the words. the Trie data structure uses a dict data structure to hold the characters.

Time Complexity:
Class TrieNode:
insert() —> O(1)
suffixes() —> O(n) where n is the char in children
Class Trie:
insert() —> O(n) where n is the number of char in words
find() —> O(c) where c is number of character in prefix

Space Complexity:
O(Total number of words in dict)