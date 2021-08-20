from environment import Environment
from simple_agent import SimpleAgent
from random_agent import RandomAgent
import random

def main():

    dim: int = 2
    rate: float = 0.1
    x: int = random.randint(0,dim-1)
    y: int = random.randint(0,dim-1)
    values_simple: list = []
    values_random: list = []

    for _ in range(7):
        print("Dim: ",dim)
        for __ in range(4):
            print("Dirt rate: ", rate)
            env_simple: Environment = Environment(dim,dim,x,y,rate)
            env_random: Environment = Environment(dim,dim,x,y,rate)
            ag_s: SimpleAgent = SimpleAgent(env_simple)
            ag_r: RandomAgent = RandomAgent(env_random)
            ag_s.think()
            ag_r.think()
            print("Reflexible agent: ", env_simple.get_performance())
            print("Random agent: ", env_random.get_performance())
            rate *= 2
        rate = 0.1
        dim *= 2
    """
    print("Simple agent")
    print("Before")
    env_simple.print_environment()
    ag_s.think()
    print("After")
    env_simple.print_environment()
    print(env_simple.get_performance())

    print("Random agent")
    print("Before")
    env_random.print_environment()
    ag_r.think()
    print("After")
    env_random.print_environment()
    print(env_random.get_performance())
    """

if __name__ == "__main__":
    main()
