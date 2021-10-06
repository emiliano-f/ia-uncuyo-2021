from board_csp import BoardCSP

def backtracking_csp(_csp: BoardCSP) -> list:
    return rec_backtraking_csp(_csp, [], 0)[1]

def rec_backtraking_csp(_csp: BoardCSP, _assignment: list, _idx: int) -> tuple:
    if _idx >= len(_csp.board):
        return (True, _assignment)

    # Select-unassigned variable: _idx
    for _ in _csp.domain:
        if is_consistent(_, _assignment, len(_csp.board)):
            _assignment.append(_)
            _csp.constraints[_] = False # arc
            result: tuple = rec_backtraking_csp(_csp, _assignment, _idx+1)
            if result[0]:
                return result
            else:
                _csp.constraints[_] = True
                _assignment.pop(len(_assignment)-1)

    return (False, _assignment)

def is_consistent(_value: int, _assignment: list, _size: int) -> bool:
    #consistent in rows y diagonal
    for _ in range(len(_assignment)):
        if _assignment[_] == _value:
            return False

    i: int = 1
    for _ in range(len(_assignment)-1,-1,-1):
        if _ < 0 or _value-i < 0:
            break
        if _value-i == _assignment[_]:
            return False
        i += 1

    i = 1
    for _ in range(len(_assignment)-1,-1,-1):
        if _ < 0 or _value+i >= _size:
            break
        if _value+i == _assignment[_]:
            return False
        i += 1

    return True
