#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 07:49:53 2021

@author: emiliano
"""
class Node:
    def __init__(self, _attribute):
        self.root: str = _attribute
        self.leaf: list = []
        
    def add_leaf(self, _subset: str, _decision: str) -> None:
        self.leaf.append((_subset, _decision))
        
class Tree:
    def __init__(self):
        self.root: list = []
        
    def add_root(self, _node: Node) -> Node:
        node: Node = Node(_node)
        self.root.append(node)
        return node
    
    def show(self) -> None:
        for leaf in self.root:
            print(leaf.root)
            for sub in leaf.leaf:
                print("\t" + str(sub))