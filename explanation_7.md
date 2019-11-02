Problem 7:
Similar to Trie (Autocomplete problem _5) the RouteTrie class and RouteTrie class have similar methods New class Router is add with the following methods:

add_handler() —> adds the path to the Trie.

lookup() —> looks up the path store in Trie data structure

_splitter() is a helper function for splitting the path string separated by “/“

Time Complexity:

Class RouteTrieNode:
insert() —> O(1)
suffixes() —> O(n) where n is the char in children

Class RouteTrie:
insert() —> O(n) where n is the number of char in words
find() —> O(c) where c is number of character in prefix

Class Router:
add handler() —> O(number of path string)
lookup() —> O(1)
_splitter() —>O(number of splits)

Space Complexity:
O(Number of path splits + number of paths)