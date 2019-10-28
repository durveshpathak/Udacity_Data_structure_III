#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:49:33 2019

@author: durvesh
"""

class RouteTrieNode():
    def __init__(self):
        self.children = {}
        self.handler = None
        
    def insert(self, path_string):
        
        if path_string not in self.children:
            self.children[path_string] = RouteTrieNode()
        else:
            pass
        

class RouteTrie():
    
    def __init__(self, root_handler):
        
        self.root = RouteTrieNode()
        self.handler = root_handler
        
    def insert(self, path, handler):
        
        node = self.root
        
        for path_string in path:
            node.insert(path_string)
            node = node.children[path_string]
        node.handler = handler
        
    def find(self, path):
        
        node = self.root
        for path_string in path:
            
            if path_string not in node.children:
                return None
            node = node.children[path_string]
        return node.handler


class Router():
    
    def __init__(self, root_handler, not_found_handler):
        
        self.router = RouteTrie(root_handler=root_handler)
        self.not_found_handler = not_found_handler
        
    def add_handler(self, raw_path, handler):
        path = self._splitter(raw_path)
        self.router.insert(path = path, handler = handler)
        
    def lookup(self, raw_path):
        
        path = self._splitter(raw_path)
        
        if len(path) == 0:
            return  self.router.handler
        
        hit = self.router.find(path = path)
        
        if hit is None:
            return self.not_found_handler
        else:
            return hit
        
        
        
    def _splitter(self,raw_path):
        finalresult = []
        result = raw_path.split(sep='/')
        
        for elem in result:
            if elem !='':
                finalresult.append(elem)
        return finalresult
    
  
#Test Case 1
router = Router("root handler", "Error 404") 
router.add_handler("/root/final_Webpage", "Final_webpage")
print(router.lookup("/"))
# root handler
print(router.lookup("/home")) 
# Error 404
print(router.lookup("/root")) 
# Error 404
print(router.lookup("/root/final_Webpage")) 
# Final_Webpage
print(router.lookup("/root/final_Webpage/")) 
# Final_Webpage
print(router.lookup("/MyWebpage/Durvesh/interest"))
# Error 404

# Test Case 2
router.add_handler("/MyWebpage/Durvesh/interest", "interest handler")
print(router.lookup("/"))
# root handler
print(router.lookup("/home")) 
# Error 404
print(router.lookup("/root")) 
# Error 404
print(router.lookup("/root/final_Webpage")) 
# Final_Webpage
print(router.lookup("/root/final_Webpage/")) 
# Final_Webpage
print(router.lookup("/MyWebpage/Durvesh/interest"))
# interest handler

# Test Case 3
router.add_handler("/TestPage", "test handler")
print(router.lookup("/"))
# root handler
print(router.lookup("/home")) 
# Error 404
print(router.lookup("/root")) 
# Error 404
print(router.lookup("/root/final_Webpage")) 
# Final_Webpage
print(router.lookup("/root/final_Webpage/")) 
# Final_Webpage
print(router.lookup("/TestPage"))
# test handler


      