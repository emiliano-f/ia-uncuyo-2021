from backtracking_csp import backtracking_csp
from board_csp import BoardCSP
from board_fc import BoardFC
from forward_checking import forward_checking

def main():

    for size in [4, 8, 10, 12, 15]:

        ## Backtracking CSP
        #backtracking: BoardCSP = BoardCSP(size)
        #print(backtracking_csp(backtracking))

        ## Forward Checking
        fc_board: BoardFC = BoardFC(size)
        print(forward_checking(fc_board))


if __name__ == '__main__':
    main()
