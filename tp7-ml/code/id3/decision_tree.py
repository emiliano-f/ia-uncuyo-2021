#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:39:07 2021

@author: emilianof_
"""
import math
from attributes import Attributes
from subsets import SubSets
from examples import Examples
from tree import Tree, Node

def decision_tree(tree: Tree, 
                  attributes: Attributes,  
                  default: str):
    
    if attributes.examples_length() == 0:
        return default
    elif attributes.examples_have_same_classification():
        return attributes.examples_unique_classification()
    elif attributes.is_empty():
        return attributes.examples_major_classification()
    else:
        best = attribute_select(attributes, attributes.examples)
        attributes.delete_attribute(best)
        subtree: Node = tree.add_root(best) # new tree with root attribute best
        m: str = attributes.dic_attributes[best].major_classification_in_subset(attributes.examples)
        # List of examples deleted
        examples_deleted: list
        for subset in attributes.dic_attributes[best].subsets:
            examples_deleted = attributes.select_subset(best, subset)
            decision: str = decision_tree(tree, attributes, m)
            attributes.restore_examples(examples_deleted)
            subtree.add_leaf(subset, decision)
        return best
    
def attribute_select(_att: Attributes, _examples: list[Examples]) -> str:
    """ Returns name of attribute selected """
    
    def maximum() -> str:
        """ Returns name of attribute with the highest gain """
        
        max_name = gain[0][0]
        max_gan = gain[0][1]
        for _ in range(1, len(gain)):
            temp_gan = gain[_][1]
            if temp_gan > max_gan:
                max_gan = temp_gan
                max_name = gain[_][0]
        return max_name

    # Entropy for examples availables
    entropy: float = I(_att.true_length(), _att.false_length())
    # Gains of each attribute
    gain: list[tuple] = []
    # Temp
    resto: float
    # Name of attribute
    name: str
    # (attribute_name, gain_attribute)
    pair: tuple
    
    for name in _att.attributes:
        attribute: SubSets = _att.dic_attributes[name]
        resto = 0
        for _ in range(len(attribute.subsets)):
            E: str = attribute.subsets[_]
            pair = attribute.counter(E, _att.examples)
            print(E, pair)
            resto += (pair[0] + pair[1])/_att.examples_length() * I(pair[0], pair[1])
        gain.append((name, entropy-resto))

    return maximum()
            
def I(pos: float, neg: float) -> float:
    """ Entropy """
    if pos == 0 and neg == 0: # When take empty subsets
        return 0.0
    coc_pos: float = pos/(pos + neg)
    coc_neg: float = neg/(pos + neg)
    first: float = 0.0
    second: float = 0.0
    if coc_pos != 0:
        first = - coc_pos*math.log(coc_pos, 2)
    if coc_neg != 0:
        second = - coc_neg*math.log(coc_neg, 2)
    return first + second
