#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:39:07 2021

@author: emilianof_
"""
import math
from base import Attributes, Examples, Examplees
from tree import Tree

def decision_tree(tree: Tree, 
                  attributes: Attributes, 
                  examples: Examples, 
                  default: int):
    
    if attributes.examples_length():
        return default
    elif examples.has_same_classification():
        return examples.major_classification
    elif attributes.is_empty():
        return valor_mayoria(examples)
    else:
        best = attribute_select(attributes, attributes.examples)
        attributes.delete(best)
        tree = create_tree(best) # new tree with root attribute best
        m = valor_mayoria(examples)
        
        
def attribute_select(_att: Attributes, _examples: list[Examplees]) -> str:
    
    def maximum() -> str:
        max_name = ganancia[0][0]
        max_gan = ganancia[0][1]
        for _ in range(1, len(ganancia)):
            temp_gan = ganancia[_][1]
            if temp_gan > max_gan:
                max_gan = temp_gan
                max_name = ganancia[_][0]
        return max_name

    entropy: float = I(_att.true_length(), _att.false_length())
    ganancia: list[tuple] = []
    resto: float

    name: str
    pair: tuple
    
    for name in _att.attributes:
        attribute = _att.dic_attributes[name]
        resto = 0
        for E in range(len(attribute.subsets)):
            pair = attribute.counter(E, _att.examples)
            resto += (pair[0] + pair[1])/_att.length * I(pair[0], pair[1])
        ganancia.append((name, entropy-resto))

    return maximum()
            
def I(pos: float, neg: float) -> float:
    coc_pos: float = pos/(pos + neg)
    coc_neg: float = neg/(pos + neg)
    return -coc_pos*math.log(coc_pos, 2) - coc_neg*math.log(coc_neg, 2)
