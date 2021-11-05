from pandas.core.frame import DataFrame
from examples import Examples

class SubSets:
    
    def __init__(self, _column: DataFrame):
        
        def names_subsets() -> list:
            return list(dict.fromkeys(column_list))
        
        # List of all subsets (including repeats) in order
        column_list: list = _column.values.tolist()
        self.rows = column_list
        
        # Subsets (without repeating)
        self.subsets = names_subsets()
        
        # Number of subsets
        self.__length__ = len(self.subsets)
        
    def is_empty(self):
        return (self.__length__ == 0)
    
    def counter(self, _subset: str, _examples: list[Examples]) -> tuple:
        """ Calculates positives and negatives of current _subset in _examples
        (only availables) """
        
        # Initialization
        count_true: int = 0
        count_false: int = 0
        # For each in _examples list (_examples[Examples])
        for _ in range(len(_examples)):
            # If row with subset is equal to _subset to calculate
            if self.rows[_] == _subset:
                # If the row belongs to the set of available examples
                if _examples[_].is_available():
                    # Final decision
                    if _examples[_].get_decision() == "yes":
                        count_true += 1
                    else:
                        count_false += 1
                
        return (count_true, count_false)
    
    def major_classification_in_subset(self, _examples: list) -> str:
        """ Returns major classification in current subset """
        
        values: tuple
        positives: int = 0
        negatives: int = 0
        for subset in self.subsets:
            values = self.counter(self, subset, _examples)
            positives += values[0]
            negatives += values[1]
        
        return "yes" if positives > negatives else "no"