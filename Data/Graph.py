import dataclasses
from collections import defaultdict
from typing import Any, Set, Iterable, Tuple, List, DefaultDict, Dict


@dataclasses.dataclass
class Vertex():
    v_id: int
    value: Any = None

    def __init__(self, v_id: int, value: Any = None):
        """
        Initializes a Vertex object.

        Params:
            v_id (int): ID of the vertex, should be a positive integer.
            value (Any): Optional value associated with the vertex.

        Raises:
            Exception: If v_id is not a positive integer.
        """
        if (not isinstance(v_id, int) and v_id < 0):
            raise Exception("Vertex ID should be a positive integer")

        self.v_id = v_id
        self.value = value

    def __hash__(self):
        """
        Returns the hash of the vertex ID.

        Returns:
            int: Hash of the vertex ID.
        """
        return hash(self.v_id)


@dataclasses.dataclass(frozen=True)
class Edge():
    target: int
    weight: float


class Graph():
    """
    Graph Data Structure

    Protected Variables:
        _vertices (Set[Vertex]): Set of Vertices
        _edges (List[Tuple[Vertex, Vertex]]): List of edges of graph, where each edge is a Vertex, Vertex pair
    """

    def __init__(self,
                 vertices: Iterable[Vertex | Any],
                 edges: Iterable[Tuple[int, int, float]]
                 ):
        """
        Constructor

        Params:
            vertices (Iterable[Vertex | Any]): List of vertices of graph, duplicate vertices will be eliminated
            edges (Iterable[Tuple[int, int, float]]): List of vertex pairs, representing the edges of graph

        Raises:
            Exception: If a node of a vertex doesn't exist in the vertex set

        Functionality:
            Initializes the following variables:
                Protected:
                    _vertices (List[Vertex]): List of Unique Vertices
                    _edges (DefaultDict[int, List[Edge]]): Lookup table for neighbours of a vertex
                    _size (int): Number of vertices
                    _num_edges (int): Number of edges between vertices
        """
        if (isinstance(vertices, Iterable)):
            if(not vertices):
                self._vertices: List[Vertex] = []

            elif all(isinstance(vertex, Vertex) for vertex in vertices):
                self._vertices: List[Vertex] = [vertex for vertex in set(vertices)]

            elif all(isinstance(vertex, int) for vertex in vertices):
                self._vertices: List[Vertex] = [Vertex(v_id=idx + 1, value=data) for idx, data in
                                                enumerate(set(vertices))]

            else:
                raise Exception("Vertices Should be of type Iterable[Vertex | Any]")
        else:
            raise Exception("Vertices Should be of type Iterable[Vertex | Any]")

        if (isinstance(edges, Iterable)):

            if(not edges):
                self._edges: DefaultDict[int, List[Edge]] = defaultdict(list)

            elif all(isinstance(edge, Tuple) for edge in edges):
                if all(isinstance(edge[0], int) and isinstance(edge[1], int) for edge in edges):
                    self._edges: DefaultDict[int, List[Edge]] = defaultdict(list)
                    for edge_tuple in edges:
                        source = edge_tuple[0]
                        target = edge_tuple[1]
                        if (len(edge_tuple) == 3):
                            weight = edge_tuple[2]
                        elif (len(edge_tuple) == 2):
                            weight = 1
                        else:
                            raise Exception(
                                "Edges Should be of type Iterable[Tuple[int, int]] or Iterable[Tuple[int, int, float]]")

                        if not (self.does_vertex_exist(source) != None and self.does_vertex_exist(target) != None):
                            raise Exception("An End Point of Vertex Doesn't Exist in Vertex Set")

                        edge = Edge(target=target, weight=weight)
                        self._edges[source].append(edge)
                else:
                    raise Exception("Edges Should be of type Iterable[Tuple[int, int]]")
            else:
                raise Exception("Edges Should be of type Iterable[Tuple[int, int]]")
        else:
            raise Exception("Edges Should be of type Iterable[Tuple[int, int]]")

        self._size: int = len(self._vertices)
        self._num_edges: int = len(self._edges)

        self._create_adjacency_matrix()

    @staticmethod
    def from_adjacency_matrix(adj_matrix: [List[List[float]]]):

        num_vertices = len(adj_matrix)

        vertices = [Vertex(v_id=i+1, value=None) for i in range(num_vertices)]


        graph=Graph(vertices,[])
        for source in range(num_vertices):
            for target in range(num_vertices):

                weight = adj_matrix[source][target]

                if weight != 0:

                    graph.add_edge(source+1, target+1, weight)
        

        return graph



    def _create_adjacency_matrix(self) -> None:
        """
        A helper function to create adjacency matrix representation of graph during constructor call.

        Params:
            None

        Functionality:
            Creates adjacency matrix:
                _adjacency_matrix (np.ndarray[int])
        """

        adjacency_matrix = [[0] * self.graph_size for _ in range(self.graph_size)]

        for vertex in self._vertices:
            current_index = vertex.v_id - 1
            for neighbour in self._edges[vertex.v_id]:
                neighbour_index = neighbour.target - 1

                adjacency_matrix[current_index][neighbour_index] = neighbour.weight

        self._adjacency_matrix = adjacency_matrix

    def get_vertex_data(self, vertex_id: int) -> Vertex | None:
        """
        Retrieves the data associated with a vertex.

        Params:
            vertex_id (int): ID of the vertex.

        Returns:
            Vertex: Data associated with the vertex, or None if the vertex does not exist.
        """
        for v in self._vertices:
            if (v.v_id == vertex_id):
                return v.value
        return None

    def set_vertex_data(self, vertex_id, value: Any) -> None:
        for v in self._vertices:
            if v.v_id == vertex_id:
                v.value = value

    def add_vertex(self, data):

        self._size += 1

        vertex = Vertex(self.graph_size, data)

        self._vertices.append(vertex)

        for row in self._adjacency_matrix:
            row.append(0)

        self._adjacency_matrix.append([0]*self.graph_size)

    def add_edge(self, source: int, target: int, weight: float):

        targets = [edge.target for edge in self._edges[source]]

        if (target not in targets):

            self._edges[source].append(Edge(target=target, weight=weight))


            self._adjacency_matrix[source-1][target-1] = weight

            self._num_edges += 1


    def get_neighbours(self, vertex_id: int) -> List[Edge]:
        """
        Retrieves the neighbours of a vertex.

        Params:
            vertex_id (int): ID of the vertex.

        Returns:
            List[Edge]: List of edges representing the neighbours of the vertex.
        """
        return self._edges[vertex_id]

    def does_vertex_exist(self, vertex_id: int) -> bool:
        """
        Checks if a vertex exists in the graph.

        Params:
            vertex_id (int): ID of the vertex.

        Returns:
            bool: True if the vertex exists, False otherwise.
        """
        return vertex_id in [v.v_id for v in self._vertices]

    @property
    def edges(self):
        """
        Retrieves the list of edges in the graph.

        Returns:
            List[Tuple[int, int, float]]: List of edges in the graph.
        """
        edge_list = []
        for source, s_edges in self._edges.items():
            for e in s_edges:
                edge_list.append((source, e.target, e.weight))
        return edge_list

    @property
    def vertices(self):
        """
        Retrieves the list of vertices in the graph.

        Returns:
            List[int]: List of vertex IDs in the graph.
        """
        return [vertex.v_id for vertex in self._vertices]

    @property
    def graph_size(self):
        """
        Retrieves the size of the graph.

        Returns:
            int: Number of vertices in the graph.
        """
        return self._size

    @property
    def adjacency_matrix(self):
        """
        Retrieves the adjacency matrix of the graph.

        Returns:
            np.ndarray[int]: Adjacency matrix of the graph.
        """
        return self._adjacency_matrix.copy()


if (__name__ == "__main__"):
    a = [[0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1],
                    [0, 0, 1, 1, 0]]

    g = Graph.from_adjacency_matrix(a)
