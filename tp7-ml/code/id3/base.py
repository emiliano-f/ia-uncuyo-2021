#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:39:07 2021

@author: emilianof_

Description: methods for decision-tree algorithm.
"""

from pandas.core.frame import DataFrame

def majority_value() -> int:
    return 0

def has_same_classification(examples: Examples) -> bool:
    
    return (examples.length == 0)
    
class Attributes:
    
    def __init__(self, df: DataFrame):
        
        def load_attributes() -> dict:
            
            attributes: dict = {}
            column: str
            for _ in range(len(columns)-1):
                column = columns[_]
                attributes[column] = SubSets(df[column], goal)
            return attributes
        
        def counter() -> None:
            for decision in goal:
                if decision == "yes":
                    self.true_length += 1
                else:
                    self.false_length += 1
                    
        columns: list = list(df.columns.values)
        goal_name: str = columns[len(columns)-1]
        goal: list = df[goal_name].values.tolist()
        
        self.attributes = columns
        self.dic_attributes = load_attributes()
        
        self.examples = [Examples(_) for _ in goal]
        self.__universe__ = len(goal)
        self.__true_length__ = 0
        self.__false_length__ = 0
        
        counter()
        
        

    def length(self) -> int:
        return self.__universe__
    
    def true_length(self) -> int:
        return self.__true_length__
    
    def false_length(self) -> int:
        return self.__false_length__
    
    def delete_attribute(self, _attribute: str) -> None:
        
        # remove name of column (ignoring key)
        self.attributes.remove(_attribute)
        """
        # save content of dictionary's key
        att_content: Examples = self.dic_attributes[_attribute]
        # delete key and content of dictionary
        self.dic_attributes.popitem(_attribute)"""
        
    #def delete_subset(self, _attribute: str, _subset: str) -> None:
        
        
class SubSets:
    
    def __init__(self, column: DataFrame, goal: list):
        
        def names_subsets() -> list:
            return list(dict.fromkeys(column_list))
            
        """ not used
        def load_examples() -> dict:
            names: dict = {}
            for example in column_list:
                names[example] = Example(example, column_list, goal)
        """
        
        column_list: list = column.values.tolist()
        self.subsets = names_subsets()
        self.rows = column_list
        self.length = len(self.subsets)
        
    def is_empty(self):
        return (self.__length__ == 0)
    
    def counter(self, _subset: str, _examples: list) -> tuple:
        count_true: int = 0
        count_false: int = 0
        for _ in range(len(_examples)):
            if self.rows[_] == _subset:
                if _examples[_].is_available():
                    if _examples[_].get_decision() == "yes":
                        count_true += 1
                    else:
                        count_false += 1
                
        return (count_true, count_false)

class Examples:
    
    def __init__(self, _example: str):
        self.__value__ = _example
        self.__available__ = True
    
    def is_available(self) -> bool:
        return self.__available__
        
    def to_available(self) -> None:
        self.__available__ = True
        
    def not_available(self) -> None:
        self.__available__ = False
        
    def get_decision(self) -> str:
        return self.__value__
    
        
        
        