#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:39:07 2021

@author: emilianof_

Description: class and some methods for decision-tree algorithm.
"""

from pandas.core.frame import DataFrame
from subsets import SubSets
from examples import Examples

class Attributes:
    
    def __init__(self, df: DataFrame):
        
        def load_attributes() -> dict:
            """ Links each attribute to its subsets """
            
            # Dict to return
            attributes: dict = {}
            # column contains name of key
            column: str
            for _ in range(len(columns)-1):
                column = columns[_]
                # Links attribute to its subset
                attributes[column] = SubSets(df[column])
            return attributes
        
        def counter() -> None:
            """ Calculates positives and negatives of initial examples """
            
            for decision in goal:
                if decision == "yes":
                    self.__true_length__ += 1
                else:
                    self.__false_length__ += 1
                    
        # List of attributes
        columns: list = list(df.columns.values)
        
        # Goal list
        goal_name: str = columns[len(columns)-1]
        goal: list = df[goal_name].values.tolist()
        
        # Save list of attributes
        self.attributes = columns
        
        # Load and save each subset of each attribute
        self.dic_attributes = load_attributes()
        
        # List of all examples
        self.examples = [Examples(_) for _ in goal]
        
        # Length of current examples
        self.__universe__ = len(goal)
        
        # Positive examples
        self.__true_length__ = 0
        
        # Negative examples
        self.__false_length__ = 0
        
        counter()
        
        

    def examples_length(self) -> int:
        """ Length of current examples """
        return self.__universe__
    
    def true_length(self) -> int:
        """ Length of positives in current examples """
        return self.__true_length__
    
    def false_length(self) -> int:
        """ Length of negatives in current examples """
        return self.__false_length__
    
    def delete_attribute(self, _attribute: str) -> None:
        """ Ignores an attribute by deleting it from the list of attributes """
        
        # remove name of column (ignoring key)
        self.attributes.remove(_attribute)
        """
        # save content of dictionary's key
        att_content: Examples = self.dic_attributes[_attribute]
        # delete key and content of dictionary
        self.dic_attributes.popitem(_attribute)"""
        
    def counter(self) -> tuple:
        """ Calculates positives and negatives in current examples """
        
        self.__true_length__ = 0
        self.__false_length__ = 0
        
        for example in self.examples:
            if example.is_available():
                if example.get_decision() == "yes":
                    self.__true_length__ += 1
                else:
                    self.__false_length__ += 1
        
        return (self.__true_length__, self.__false_length__)
                        
    
    def examples_have_same_classification(self) -> bool:
        """ If all are positives (or negatives) returns True """
        return (self.true_length()==0 or self.false_length()==0)
        
    def examples_unique_classification(self) -> str:
        """ Returns unique decision available """
        return "yes" if self.true_length() == 0 else "no"
    
    def examples_major_classification(self) -> str:
        """ Returns majority classification (attributes empty) """
        return "yes" if self.true_length() > self.false_length() else "no"
        
    def select_subset(self, _attribute: str, _subset: str) -> list:
        """ Selects subset retaining examples in it """
        
        deleted: list = []
        for _ in range(len(self.examples)):
            # Access to attribute's row
            if self.dic_attributes[_attribute].rows[_] != _subset:
                if self.examples[_].is_available():
                    self.examples[_].not_available()
                    deleted.append(_)
        self.counter()
        return deleted
    
    def restore_examples(self, _restore: list) -> None:
        """ Restores examples in list _restore """
        
        for _ in _restore:
            self.examples[_].to_available()
        self.counter()
        

        

