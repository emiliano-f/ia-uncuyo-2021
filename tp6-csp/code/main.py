from backtracking_csp import backtracking_csp
from board_csp import BoardCSP
from board_fc import BoardFC
from forward_checking import forward_checking
from time import time

import csv
import statistics as stats

def main():
    it: int = 100
    init: float = 0
    sizes_bt: list = []
    sizes_fc: list = []
    states_bt: list = []
    states_fc: list = []

    values: tuple[int, list]

    for size in [4, 8, 10, 12, 15]:
        times_bt: list = []
        times_fc: list = []
        stt_bt: list = []
        stt_fc: list = []
        sizes_bt.append((size,times_bt))
        sizes_fc.append((size,times_fc))
        states_bt.append((size,stt_bt))
        states_fc.append((size,stt_fc))
        for _ in range(it):
            ## Backtracking CSP
            backtracking: BoardCSP = BoardCSP(size)
            init = time()
            values = backtracking_csp(backtracking)
            #print(values[1])
            stt_bt.append(values[0])
            times_bt.append(time() - init)

        for _ in range(it):
            ## Forward Checking
            fc_board: BoardFC = BoardFC(size)
            init = time()
            values = forward_checking(fc_board)
            #print(values[1])
            stt_fc.append(values[0])
            times_fc.append(time() - init)

    title_time: list = ["time "+str(_) for _ in range(100)]
    title_state: list = ["state "+str(_) for _ in range(100)]

    with open("out_bt.csv", "w") as csp_file:
        csp_writer = csv.writer(csp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csp_writer.writerow(title_time)
        for _ in range(len(sizes_bt)):
            csp_writer.writerow(sizes_bt[_][1])

        csp_writer.writerow(title_state)
        for _ in range(len(states_bt)):
            csp_writer.writerow(states_bt[_][1])

    with open("out_fc.csv", "w") as csp_file:
        csp_writer = csv.writer(csp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csp_writer.writerow(title_time)
        for _ in range(len(sizes_fc)):
            csp_writer.writerow(sizes_fc[_][1])

        csp_writer.writerow(title_state)
        for _ in range(len(states_fc)):
            csp_writer.writerow(states_fc[_][1])

    for _ in range(len(sizes_bt)):
        print(stats.mean(sizes_bt[_][1]))
        print(stats.mean(sizes_fc[_][1]))


if __name__ == '__main__':
    main()
