#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:39:07 2021

@author: emilianof_
"""
import math
from base import Attributes, Examples, SubSets
from tree import Tree

def decision_tree(tree: Tree, 
                  attributes: Attributes,  
                  default: str):
    
    if attributes.examples_length():
        return default
    elif attributes.examples_has_same_classification():
        return attributes.examples_unique_classification()
    elif attributes.is_empty():
        return attributes.examples_major_classification()
    else:
        best = attribute_select(attributes, attributes.examples)
        attributes.delete_attribute(best)
        #tree = create_tree(best) # new tree with root attribute best
        m = attributes.dic_attributes[best].major_classification_in_subset(attributes.examples)
        # List of examples deleted
        examples_deleted: list
        for subset in attributes.dic_attributes[best].subsets:
            examples_deleted = attributes.select_subset(best, subset)
            subarbol = decision_tree(tree, attributes, m)
            attributes.restore_examples(examples_deleted)
        
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
        attribute = _att.dic_attributes[name]
        resto = 0
        for E in range(len(attribute.subsets)):
            pair = attribute.counter(E, _att.examples)
            resto += (pair[0] + pair[1])/_att.length * I(pair[0], pair[1])
        gain.append((name, entropy-resto))

    return maximum()
            
def I(pos: float, neg: float) -> float:
    """ Entropy """
    coc_pos: float = pos/(pos + neg)
    coc_neg: float = neg/(pos + neg)
    return -coc_pos*math.log(coc_pos, 2) - coc_neg*math.log(coc_neg, 2)
