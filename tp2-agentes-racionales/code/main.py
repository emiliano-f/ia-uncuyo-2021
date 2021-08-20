from environment import Environment
from simple_agent import SimpleAgent
from random_agent import RandomAgent

def main():

    env_simple: Environment = Environment(64,64,1,1,0.5)
    env_random: Environment = Environment(64,64,1,1,0.5)
    ag_s: SimpleAgent = SimpleAgent(env_simple)
    ag_r: RandomAgent = RandomAgent(env_random)

    print("Simple agent")
    print("Before")
    env_simple.print_environment()
    ag_s.think()
    print("After")
    env_simple.print_environment()

    print("Random agent")
    print("Before")
    env_random.print_environment()
    ag_r.think()
    print("After")
    env_random.print_environment()

if __name__ == "__main__":
    main()
