#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:03:18 2019

@author: durvesh
"""

class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = {}
        
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            
        else:
            pass
        
    def suffixes(self, suffix = ''):
        stored_suffix = []
        
        if self.is_word and suffix!= '':
            stored_suffix.append(suffix)
        if len(self.children) == 0:
            return stored_suffix
        for char in self.children:
            stored_suffix.extend(self.children[char].suffixes(suffix=suffix+char))
        return stored_suffix
            
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        
        node = self.root
        
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True
        
    def find(self, prefix):
        
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthropology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + "not found")
    else:
        print('')
        
#Test Case 1
interact(f,prefix='a');
"""
nt
ntagonist
ntonym
nthropology
"""

 
#Test Case 3
interact(f,prefix='tr');
"""
ipod
igonometry
igger
ie
"""
#Test Case 4
interact(f,prefix='');
"""
"""
