from typing import Tuple, Any, List
from Data import Graph
from math import inf

def belmannford(graph: Graph, start: int, end: int) -> Tuple[int]:
    """
    Runs the Bellman-Ford Algorithm to find the shortest path from start vertex to end vertex.

    Params:
        graph (Graph): Graph to be searched for
        start (int): id of the start vertex
        end (int): id of the end vertex

    Returns:
        Tuple[int]: path from start vertex to end vertex
    """
    distances = graph.graph_size * [inf]
    distances[start - 1] = 0

    parents = graph.graph_size * [-1]

    for i in range(graph.graph_size):

        for edge in graph.edges:
            source, target, weight = edge
            if (distances[target - 1] > distances[source - 1] + weight):
                distances[target - 1] = distances[source - 1] + weight
                parents[target - 1] = source

        for edge in graph.edges:
            source, target, weight = edge
            if (distances[target - 1] > distances[source - 1] + weight):
                return []

        temp = end
        path = []

        while (temp != start):
            path.append(temp)
            temp = parents[temp - 1]

        path.append(start)

        return tuple(reversed(path))


def dijkstra(graph: Graph, start: int, end: int):
    """
    Runs the Dijkstra Algorithm to find the shortest path from start vertex to end vertex.

    Params:
        graph (Graph): Graph to be searched for
        start (int): id of the start vertex
        end (int): id of the end vertex

    Returns:
        Tuple[int]: path from start vertex to end vertex
    """
    distances = graph.graph_size * [inf]
    distances[start - 1] = 0

    parents = graph.graph_size * [-1]

    to_be_covered = graph.vertices

    while to_be_covered:

        min_distanced_vertex = to_be_covered[0]
        min_distance = 0

        for i in range(1, len(to_be_covered)):

            vertex = to_be_covered[i]

            if (min_distance > distances[vertex - 1]):
                min_distanced_vertex = vertex
                min_distance = distances[vertex - 1]

        to_be_covered.remove(min_distanced_vertex)

        for neighbour in graph.get_neighbours(min_distanced_vertex):
            target = neighbour.target
            weight = neighbour.weight

            if (distances[target - 1] > distances[min_distanced_vertex - 1] + weight):
                distances[target - 1] = distances[min_distanced_vertex - 1] + weight
                parents[target - 1] = min_distanced_vertex

    temp = end
    path = []

    while (temp != start):
        path.append(temp)
        temp = parents[temp - 1]

    path.append(start)

    return tuple(reversed(path))


def floydwarshall(graph: Graph):
    """
    Runs the Floyd-Warshall Algorithm to find the shortest paths between all pairs of vertices.

    Params:
        graph (Graph): Graph to be searched for

    Returns:
        List[List[float]]: matrix of shortest path lengths between all pairs of vertices
    """
    adj_matrix = graph.adjacency_matrix

    path_lenght_matrix = [[adj_matrix[i][j] if adj_matrix[i][j] != 0 else inf for j in range(graph.graph_size)]
                          for i in range(graph.graph_size)]

    temp = [[None for j in range(graph.graph_size)]
            for i in range(graph.graph_size)]

    for m in range(graph.graph_size):
        for i in range(graph.graph_size):
            for j in range(graph.graph_size):

                temp[i][j] = min(path_lenght_matrix[i][j], path_lenght_matrix[i][m] + path_lenght_matrix[i][m])

        path_lenght_matrix = temp

    return path_lenght_matrix

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [(1, 2, 2), (1, 3, 4),
             (2, 4, 3),
             (3, 4, 1), (3, 7, 5000),
             (4, 5, 7),
             (5, 6, 2),
             (6, 7, 1),
             (7, 4, 3)]

    g = Graph(vertices, edges)

    print(belmannford(g, 1, 7))
    print(dijkstra(g, 1, 7))

    print(floydwarshall(g))

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [(1, 2, 2), (1, 3, 4),
             (2, 4, 3),
             (3, 4, 1), (3, 7, 5000),
             (4, 5, 7),
             (5, 6, 2),
             (6, 7, 1),
             (7, 4, 3)]

    g = Graph(vertices, edges)

    print(belmannford(g, 1, 7))
    print(dijkstra(g, 1, 7))

    print(floydwarshall(g))
