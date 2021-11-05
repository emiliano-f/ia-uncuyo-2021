class Examples:
    """ Definition for each final decision """
    
    def __init__(self, _example: str):
        # Decision
        self.__value__ = _example
        # Is available?
        self.__available__ = True
    
    def is_available(self) -> bool:
        return self.__available__
        
    def to_available(self) -> None:
        """ Changes availability to True """
        self.__available__ = True
        
    def not_available(self) -> None:
        """ Changes availability to False """
        self.__available__ = False
        
    def get_decision(self) -> str:
        """ Returns current availability """
        return self.__value__