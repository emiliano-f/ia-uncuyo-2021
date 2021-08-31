from agent import Agent
from environment import Environment
from dque import Queue
from graph import Graph
from random import randint
import statistics

def main():

    size: int = 100
    lim: int = size-1
    la = []

    for _ in range(100):
        env: Environment = Environment(randint(0,lim),randint(0,lim),randint(0,lim),randint(0,lim),0.3,size)
        gr: Graph = Graph(size*size)
        gr.load_environment(env)

        ag: Agent = Agent(env, gr)
        ag.load_heuristic()
        if ag.think() != None:
            la.append(ag.states)

    print(la)
    print(statistics.mean(la),statistics.stdev(la))

if __name__ == "__main__":
    main()
