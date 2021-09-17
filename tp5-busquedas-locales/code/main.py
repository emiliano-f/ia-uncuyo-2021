from hill_climbing_std import HillClimbingStd
from simulated_annealing import SimulatedAnnealing
from genetic import Genetic

def main():

    bot: HillClimbingStd = HillClimbingStd(16, 50)
    #print(bot.board, bot.get_fn())
    print(bot.think(), bot.get_fn())

    """
    sa: SimulatedAnnealing = SimulatedAnnealing(16)
    print(sa.think(), bot.get_fn())

    gen: Genetic = Genetic(8, 20, 10, 3)
    #print(gen.test())
    print(gen.think())
    """
if __name__ == "__main__":
    main()
