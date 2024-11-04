import dataclasses
from collections import defaultdict
from typing import Any,Set,Iterable,Tuple,List,DefaultDict
import numpy as np

@dataclasses.dataclass
class Vertex():
    value:Any
    is_visited:bool


class Graph():
    
    """
    Graph Data Structure
    
        Protected Variables:
            _vertices: Set[Vertex]: Set of Vertices
            _edges:List[Tuple[Vertex,Vertex]]: List of edges of graph, where each edge is a Vertex,Vertex pair
  
    """



    def __init__(self,vertices:Iterable[Vertex],edges:List[Tuple[Vertex,Vertex]]):
        
        """
        Constructor
        Params:
            vertices:Iterable[Vertex] -> List of vertices of graph, duplicate vertices will be eliminated
            edges:List[Tuple[Vertex,Vertex]] -> List of vertex pairs, representing the edges of graph

        Raises Exception When:
            An node of an vertex doesn't exist in vertice set
            
        Functionality:
            Initialises Following Variables:
                Protected:
                    _vertices:List[Vertex] -> List of Unique Vertices 
                        TODO: While implementing adding a nev vertex check uniqueness

                    _edges:DefaultDict[Vertex,List[Vertex]] -> Lookup table for neighbours of a vertex

                    _size:int -> Number of vertices

                    _num_edges:int ->number of edges between vertices
            """
        
        self._vertices:List[Vertex] = [vertex for vertex in set(vertices)]
        self._edges:DefaultDict[Vertex,List[Vertex]]=defaultdict(list)

        for edge in edges:
            
            if not(edge[0] in self._vertices and edge[1] in self._vertices):
                raise Exception("An End Point of Vertex Doesnt Exist in Vertex Set")
            
            self._edges[edge[0]].append(edge[1])


        self._size:int=len(self._vertices)
        self._num_edges:int=len(self._edges)

        self._create_adjacency_matrix()

    def _create_adjacency_matrix(self)->None:
        
        """
        A helper function to create adjacency matrix representation of graph during constructer call.
        Params:
            None

        Functionality
        creates adjacency matrix:
            _adjacency_matrix: np.ndarray[int]

        """


        adjacency_matrix=np.zeros([self._size,self._size])

        for vertex in self._vertices:
            current_index = self._vertices.index(vertex)

            for neigbour in self._edges[vertex]:
                neigbour_index=self._vertices.index(neigbour)

                adjacency_matrix[current_index][neigbour_index]=1

        self._adjacency_matrix=adjacency_matrix
    
        


if(__name__=="__main__"):

    vertices=[1,2,3,4]
    edges=[(1,2),(1,4),
            (2,1),(2,2),(2,3),(2,4),
            (3,4),
            (4,1),(4,2)]


    g=Graph(vertices,edges)

    print(g._edges)
    print(g._adjacency_matrix)   