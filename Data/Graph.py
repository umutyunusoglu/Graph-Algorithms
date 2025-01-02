import dataclasses
from collections import defaultdict
from typing import Any, Set, Iterable, Tuple, List, DefaultDict
import numpy as np


@dataclasses.dataclass
class Vertex():
    v_id: int
    value: Any = None

    def __init__(self, v_id: int, value: Any = None):
        if (not isinstance(v_id, int) and v_id < 0):
            raise Exception("Vertex ID should be a positive integer")

        self.v_id = v_id
        self.value = value

    def __hash__(self):
        return hash(self.v_id)


@dataclasses.dataclass
class Edge():
    source: Vertex
    target: Vertex
    directed: bool = False


class Graph():
    """
    Graph Data Structure
    
        Protected Variables:
            _vertices: Set[Vertex]: Set of Vertices
            _edges:List[Tuple[Vertex,Vertex]]: List of edges of graph, where each edge is a Vertex,Vertex pair
  
    """

    def __init__(self,
                 vertices: Iterable[Vertex | Any],
                 edges: Iterable[Tuple[int, int]]
                 ):

        """
        Constructor
        Params:
            vertices:Iterable[Vertex]|Any] -> List of vertices of graph, duplicate vertices will be eliminated
            edges:List[Tuple[Vertex,Vertex]] -> List of vertex pairs, representing the edges of graph

        Raises Exception When:
            An node of an vertex doesn't exist in vertice set
            
        Functionality:
            Initialises Following Variables:
                Protected:
                    _vertices:List[Vertex] -> List of Unique Vertices 
                        TODO: While implementing adding a new vertex check uniqueness

                    _edges:DefaultDict[int,List[int]] -> Lookup table for neighbours of a vertex

                    _size:int -> Number of vertices

                    _num_edges:int ->number of edges between vertices
            """

        #TODO: Implement a type checker for initialisation

        if (isinstance(vertices, Iterable)):
            if all(isinstance(vertex, Vertex) for vertex in vertices):
                self._vertices: List[Vertex] = [vertex for vertex in set(vertices)]

            elif all(isinstance(vertex, int) for vertex in vertices):
                self._vertices: List[Vertex] = [Vertex(v_id=idx + 1, value=data) for idx, data in
                                                enumerate(set(vertices))]

            else:
                raise Exception("Vertices Should be of type Iterable[Vertex|Any]")
        else:
            raise Exception("Vertices Should be of type Iterable[Vertex|Any]")



        self._edges: DefaultDict[int, Tuple[int]] = defaultdict(list)

        for edge in edges:
            source = edge[0]
            target = edge[1]

            if not (self.does_vertex_exist(source) != None and self.does_vertex_exist(target) != None):

                raise Exception("An End Point of Vertex Doesnt Exist in Vertex Set")

            self._edges[source].append(target)

        self._size: int = len(self._vertices)
        self._num_edges: int = len(self._edges)

        self._create_adjacency_matrix()

    def _create_adjacency_matrix(self) -> None:

        """
        A helper function to create adjacency matrix representation of graph during constructer call.
        Params:
            None

        Functionality
        creates adjacency matrix:
            _adjacency_matrix: np.ndarray[int]

        """

        adjacency_matrix = np.zeros([self._size, self._size])

        for vertex in self._vertices:

            current_index = self._vertices.index(vertex)

            for neigbour in self._edges[vertex.v_id]:
                neigbour_index = neigbour - 1

                adjacency_matrix[current_index][neigbour_index] = 1

        self._adjacency_matrix = adjacency_matrix

    def get_vertex_data(self, vertex_id: int) -> Vertex:

        for v in self._vertices:
            if (v.v_id == vertex_id):
                return v.value

        return None

    def get_graph_size(self) -> int:
        return self._size

    def get_neighbours(self, vertex_id: int) -> List[int]:
        return self._edges[vertex_id]

    def does_vertex_exist(self, vertex_id: int) -> bool:
        return vertex_id in [v.v_id for v in self._vertices]


if (__name__ == "__main__"):
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (1, 4),
             (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 4),
             (4, 1), (4, 2)]

    g = Graph(vertices, edges)

    print(g._edges)
    print(g._adjacency_matrix)
