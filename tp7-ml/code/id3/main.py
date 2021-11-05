#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 07:47:13 2021

@author: emiliano
"""

from load_csv import load_csv
from attributes import Attributes
from tree import Tree
from decision_tree import decision_tree

def main():
    dataframe = load_csv("tennis.csv")    
    attributes: Attributes = Attributes(dataframe)
    tree: Tree = Tree()
    decision_tree(tree, attributes, "no")
    tree.show()
    
if __name__ == "__main__":
    main()