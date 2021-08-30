from agent import Agent
from environment import Environment
from graph import Graph
from random import randint

def main():

    size: int = 10
    lim: int = size-1
    gr: Graph = Graph(size*size)
    env: Environment = Environment(randint(0,lim),randint(0,lim),randint(0,lim),randint(0,lim),0.3,size)
    gr.load_environment(env)
    #gr.show()
    env.print_environment()

    ag: Agent = Agent(env, gr)

if __name__ == "__main__":
    main()
