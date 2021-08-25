from breadth_first_search import BreadthSearchAgent
from environment import Environment
from graph import Graph
from uniform_search import UniformSearchAgent

def main():
    size: int = 10
    gr: Graph = Graph(size*size)
    env: Environment = Environment(1,1,6,5,0.2,size)
    gr.load_environment(env)
    gr.show()
    env.print_environment()

if __name__ == "__main__":
    main()
