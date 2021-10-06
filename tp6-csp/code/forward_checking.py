from board_fc import BoardFC, Link
from dque import Queue

def forward_checking(_csp: BoardFC) -> list:

    assignment: list = []
    removed: Queue = Queue()

    col: int
    row: int
    save: tuple
    column: Link
    to_restore: list[tuple]

    # First iteration
    removed.append((0, -1))
    assignment.append(0)
    ###

    while not removed.is_empty():
        to_restore = removed.pop()
        col = to_restore[0]
        row = to_restore[1]
        restore(_csp, to_restore, assignment)

        # Assignment in columns
        while col < len(_csp.board):
            row += 1 # Next element in domain
            column = _csp.board[col]
            while row < len(_csp.board) and not column.domain[row]:
                row += 1 # Try this when element isnt in domain

            if row < len(_csp.board): # if T, also column.domain[row] is T
                assignment.append(row)
                save = delete_forward(_csp, row, col)
                removed.append(save[1])
                if save[0]:
                    break
            else:
                break

            col += 1
            row = -1

        if len(assignment) == len(_csp.board):
            return assignment
    return []

def restore(_csp: BoardFC, _to_restore: tuple, _assignment: list) -> None:

    _assignment.pop()
    col: int = _to_restore[0]
    row: int = _to_restore[1]
    if row < 0:
        return

    diag_up: int
    diag_down: int
    queen_domain: list
    i: int = 1
    for _ in range(col+1, len(_csp.board)):
        queen = _csp.board[_]

        # Restore element in domain        print(size)
        diag_up = row - i
        if diag_up > -1:
            queen.restore_domain_element(diag_up)

        # Restore element in domain
        diag_down = row + i
        if diag_down < len(_csp.board):
            queen.restore_domain_element(diag_down)

        # Restore same row in domain
        queen.restore_domain_element(row)
        i += 1

def delete_forward(_csp: BoardFC, _row: int, _col: int) -> tuple:

    alert: bool = False #
    diag_up: int
    diag_down: int
    queen_domain: list
    i: int = 1
    for _ in range(_col+1, len(_csp.board)):
        queen = _csp.board[_]

        # Delete element in domain
        diag_up = _row - i
        if diag_up > -1:
            queen.delete_domain_element(diag_up)

        # Delete element in domain
        diag_down = _row + i
        if diag_down < len(_csp.board):
            queen.delete_domain_element(diag_down)

        # Delete same row in domain
        queen.delete_domain_element(_row)

        if queen.length <= 0:
            alert = True
        i += 1

    return (alert, (_col, _row))

