from typing import Tuple, Any,List
from Data import Graph
import numpy as np
from numpy.typing import ArrayLike
import dataclasses
from collections import deque


def BFS(graph: Graph, start: int, end: int) -> Tuple[int]:
    """
    Runs Breadth for Search Algorithm to find a path from start vertex to end vertex.


    Args:
        graph: Graph -> Graph to be searched for
        start: int -> id of the start vertex
        end: int -> id of the end vertex

    Returns:
        Tuple[int] -> path from start vertex to end vertex
    """

    visited = graph.get_graph_size() * [False]
    parent = graph.get_graph_size() * [-1]

    queue = deque()

    visited[start - 1] = True

    queue.append(start)

    path:List[int] = []

    while queue:
        current_vertex= queue.popleft()



        for neighbour in graph.get_neighbours(current_vertex):

            if(not visited[neighbour-1]):

                parent[neighbour-1]=current_vertex
                visited[neighbour-1]=True

                if(neighbour==end):
                    temp=neighbour
                    while(parent[temp-1]!=-1):
                        path.append(temp)
                        temp=parent[temp-1]
                    path.append(start)

                    return tuple(reversed(path))

                queue.append(neighbour)
    return tuple()


def DFS(graph: Graph, start: int, end: int) -> Tuple[int]:
    """
    Runs Depth for Search Algorithm to find a path from start vertex to end vertex.


    Args:
        graph: Graph -> Graph to be searched for
        start: int -> id of the start vertex
        end: int -> id of the end vertex

    Returns:
        Tuple[int] -> path from start vertex to end vertex
    """

    visited = graph.get_graph_size() * [False]
    parent = graph.get_graph_size() * [-1]

    stack = []

    visited[start - 1] = True

    stack.append(start)

    path = []

    while stack:

        current_vertex = stack.pop()

        for neighbour in graph.get_neighbours(current_vertex):
            if (not visited[neighbour - 1]):

                parent[neighbour - 1] = current_vertex
                visited[neighbour - 1] = True

                if (neighbour == end):
                    temp = neighbour
                    while (parent[temp - 1] != -1):
                        path.append(temp)
                        temp = parent[temp - 1]
                    path.append(start)

                    return tuple(reversed(path))

                stack.append(neighbour)
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

    print(BFS(g, 1, 3))
    print(DFS(g,1,3))

