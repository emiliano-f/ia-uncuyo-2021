from hill_climbing_std import HillClimbingStd
from simulated_annealing import SimulatedAnnealing
from genetic import Genetic
from time import time
import csv
import statistics

def main():
    rep: int = 30
    tam: int = 15
    ##################################### Hill Climbing

    times_hc = []
    prev_status = []
    cant_status_hc = []
    success_hc = 0
    for _ in range (rep):
        bot: HillClimbingStd = HillClimbingStd(tam, 50)
        init = time()
        tupla = bot.think()
        times_hc.append(time() - init)
        cant_status_hc.append(len(tupla[1]))
        prev_status.append(tupla[1])
        if tupla[0]:
            success_hc += 1

    with open("hcstd.csv", "w") as csv_file:
        hc_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for _ in prev_status:
            hc_writer.writerow(_)

    ############################### Simulated Annealing
    times_sa = []
    prev_status = []
    cant_status_sa = []
    success_sa = 0
    for _ in range (rep):
        sa: SimulatedAnnealing = SimulatedAnnealing(tam)
        init = time()
        tupla = sa.think()
        times_sa.append(time() - init)
        cant_status_sa.append(len(tupla[1]))
        prev_status.append(tupla[1])
        if tupla[0]:
            success_sa += 1

    with open("sa.csv", "w") as csv_file:
        sa_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for _ in prev_status:
            sa_writer.writerow(_)

    ################################## Genetic Algorithm

    times_ag = []
    prev_status = [] #cant_status
    success_ag = 0
    for _ in range (rep):
        gen: Genetic = Genetic(tam, 20, 10, 3)
        init = time()
        tupla = gen.think()
        times_ag.append(time() - init)
        prev_status.append(tupla[1])
        if tupla[0]:
            success_ag += 1

    with open("ag.csv", "w") as csv_file:
        ag_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ag_writer.writerow(prev_status)

    with open("statistics.txt", "w") as _file:
        _file.write("1. Hill Climbing \n2. Simulated Annealing \n3. Genetic Algorithm\n")
        _file.write("\nTimes: \n")
        _file.write(str(times_hc))
        string = "\n Promedio: " + str(statistics.mean(times_hc)) + " Desviación estandar: " + str(statistics.stdev(times_hc)) + "\n"
        _file.write(string)
        _file.write(str(times_sa))
        string = "\n Promedio: " + str(statistics.mean(times_sa)) + " Desviación estandar: " + str(statistics.stdev(times_sa)) + "\n"
        _file.write(string)
        _file.write(str(times_ag))
        string = "\n Promedio: " + str(statistics.mean(times_ag)) + " Desviación estandar: " + str(statistics.stdev(times_ag)) + "\n"
        _file.write(string)

        _file.write("\nStatus: \n")
        _file.write(str(cant_status_hc))
        string = "\n Promedio: " + str(statistics.mean(cant_status_hc)) + " Desviación estandar: " + str(statistics.stdev(cant_status_hc)) + "\n"
        _file.write(string)
        _file.write(str(cant_status_sa))
        string = "\n Promedio: " + str(statistics.mean(cant_status_sa)) + " Desviación estandar: " + str(statistics.stdev(cant_status_sa)) + "\n"
        _file.write(string)
        _file.write(str(prev_status))
        string = "\n Promedio: " + str(statistics.mean(prev_status)) + " Desviación estandar: " + str(statistics.stdev(prev_status)) + "\n"
        _file.write(string)

        _file.write("\nSuccess: \n")
        _file.write(str(success_hc) + "\n")
        _file.write(str(success_sa) + "\n")
        _file.write(str(success_ag) + "\n")

if __name__ == "__main__":
    main()
