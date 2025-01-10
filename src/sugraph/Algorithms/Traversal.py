from typing import Tuple,List
from src.sugraph.Data import Graph
from collections import deque


def BFS(graph: Graph, start: int, end: int) -> Tuple[int]:
    """
        Runs Breadth-First Search (BFS) Algorithm to find a path from start vertex to end vertex.

        Args:
            graph: Graph -> Graph to be searched for
            start: int -> id of the start vertex
            end: int -> id of the end vertex

        Returns:
            Tuple[int] -> path from start vertex to end vertex
    """

    if (isinstance(graph, Graph)):
        adj_matrix = graph.adjacency_matrix

    elif (isinstance(graph, list)):
        for row in graph:
            if (isinstance(row, list)):
                if all(isinstance(entry, float | int) for entry in row):
                    adj_matrix = graph
                else:
                    raise Exception("graph Should be of type Graph|List[List[float]]")
            else:
                raise Exception("graph Should be of type Graph|List[List[float]]")
    else:
        raise Exception("graph Should be of type Graph|List[List[float]]")

    graph_size = len(adj_matrix)


    start_index=start-1

    visited = graph_size * [False]
    visited[start_index] = True

    parent = graph_size * [-1]

    queue = deque()


    queue.append(start)

    path:List[int] = []

    while queue:
        current_vertex= queue.popleft()

        current_vertex_index=current_vertex-1

        neighbours_indices=[i for i in range(graph_size) if adj_matrix[current_vertex_index][i]!=0]

        for neighbour_index in neighbours_indices:


            if(not visited[neighbour_index]):

                parent[neighbour_index]=current_vertex
                visited[neighbour_index]=True

                if(neighbour_index+1==end):

                    temp=neighbour_index+1

                    while(parent[temp-1]!=-1):
                        path.append(temp)
                        temp=parent[temp-1]
                    path.append(start)

                    return tuple(reversed(path))

                queue.append(neighbour_index+1)
    return tuple()


def DFS(graph: Graph|List[List[float]], start: int, end: int) -> Tuple[int]:

    """
        Runs Depth-First Search (DFS) Algorithm to find a path from start vertex to end vertex.

        Args:
            graph: Graph -> Graph to be searched for
            start: int -> id of the start vertex
            end: int -> id of the end vertex

        Returns:
            Tuple[int] -> path from start vertex to end vertex
    """



    if(isinstance(graph,Graph)):
        adj_matrix=graph.adjacency_matrix

    elif(isinstance(graph,list)):
        for row in graph:
            if(isinstance(row,list)):
                if all(isinstance(entry,float|int) for entry in row):
                    adj_matrix=graph
                else:
                    raise Exception("graph Should be of type Graph|List[List[float]]")
            else:
                raise Exception("graph Should be of type Graph|List[List[float]]")
    else:
        raise Exception("graph Should be of type Graph|List[List[float]]")


    graph_size = len(adj_matrix)
    start_index = start - 1

    visited = graph_size * [False]
    visited[start_index] = True

    parent = graph_size * [-1]

    stack = []

    stack.append(start)

    path = []

    while stack:

        current_vertex = stack.pop()

        current_vertex_index=current_vertex-1

        neighbours_indices=[i for i in range(graph_size) if adj_matrix[current_vertex_index][i]!=0]

        for neighbour_index in neighbours_indices:

            if (not visited[neighbour_index]):

                parent[neighbour_index] = current_vertex
                visited[neighbour_index] = True

                if (neighbour_index+1 == end):

                    temp = neighbour_index+1

                    while (parent[temp-1] != -1):
                        path.append(temp)
                        temp = parent[temp - 1]
                    path.append(start)

                    return tuple(reversed(path))

                stack.append(neighbour_index+1)

    return tuple()

    return []


if __name__ == "__main__":
    vertices = [1, 2, 3, 4,5,6]
    edges = [(1, 2), (1, 4),
             (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 4),(3,5),
             (4, 1), (4, 2),(4,6),
             (5,3),
             (6,4)]

    g = Graph(vertices, edges)


    print(BFS(g,1,3))
    print(DFS(g,1,3))

