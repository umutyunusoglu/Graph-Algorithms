
from typing import Tuple, Any, List,DefaultDict
from Data import Graph
from math import inf
from Traversal import DFS

def fordfulkerson(graph:Graph,start,end):
    """
    Ford-Fulkerson Algorithm for finding Max Flow for integer capacities

    Args:
        graph(Graph): A weighted graph whose weights will be considered as capacities.

    Returns:
        Tuple[Tuple[Tuple[float]],int] : Flow matrix and max flow value
    """

    capacities=graph.adjacency_matrix

    flow_matrix=[[0]*graph.graph_size for _ in range(graph.graph_size)]
    residual_graph=capacities.copy()


    max_flow=0

    path=DFS(residual_graph,start,end)

    while path:
        min_capacity=inf
        for i in range(len(path)-1):
            source=path[i]
            target=path[i+1]

            if(residual_graph[source-1][target-1]<min_capacity):
                min_capacity=residual_graph[source-1][target-1]



        for i in range(len(path)-1):
            source=path[i]
            target=path[i+1]

            residual_graph[source-1][target-1]=residual_graph[source-1][target-1]-min_capacity
            residual_graph[target-1][source-1]=residual_graph[target-1][source-1]+min_capacity


            flow_matrix[source-1][target-1]=flow_matrix[source-1][target-1] + min_capacity
            flow_matrix[target-1][source-1]=-flow_matrix[source-1][target-1]

        max_flow+=min_capacity

        path=DFS(residual_graph,start,end)



    return flow_matrix,max_flow


if __name__=="__main__":

    graph=Graph.from_adjacency_matrix([[0, 3, 2, 0],
                                         [0, 0, 1, 2],
                                         [0, 0, 0, 4],
                                         [0, 0, 0, 0]])

    flow_matrix,max_flow=fordfulkerson(graph,1,3)

    print("Flow Matrix:")
    for row in flow_matrix:
        print(row)
    print("Max Flow:",max_flow)

    print("True Max Flow:",23)



