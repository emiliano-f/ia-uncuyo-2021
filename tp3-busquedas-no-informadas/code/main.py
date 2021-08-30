from breadth_first_search import BreadthSearchAgent
from environment import Environment
from depth_limited_search import DepthLimitedSearchAgent
from graph import Graph
from uniform_search import UniformSearchAgent
from random import randint
import statistics as stats
from minheap import Heap

def main():

    size: int = 100
    lim: int = size-1

    ### Breadth first search
    gr: Graph = Graph(size*size)

    env: Environment = Environment(randint(0,lim),randint(0,lim),randint(0,lim),randint(0,lim),0.3,size)
    gr.load_environment(env)
    #gr.show()
    env.print_environment()

    ag: BreadthSearchAgent = BreadthSearchAgent(env, gr)
    print("Secuencia para búsqueda en anchura: ")
    print(ag.think())

    ### Uniform search
    gr_unif: Graph = Graph(size*size)
    gr_unif.load_environment(env)
    unif: UniformSearchAgent = UniformSearchAgent(env, gr_unif)
    print("Secuencia para búsqueda uniforme: ")
    print(unif.think())

    ### Depth limited search
    gr_depth: Graph = Graph(size*size)
    gr_depth.load_environment(env)
    depth: DepthLimitedSearchAgent = DepthLimitedSearchAgent(env, gr_depth)
    print("Secuencia para búsqueda en profundidad limitada: ")
    print(depth.think())

if __name__ == "__main__":
    main()
