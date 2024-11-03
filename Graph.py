import dataclasses
from typing import Any,Set,Iterable,Tuple,List


@dataclasses.dataclass
class Node():
    value:Any
    is_visited:bool


class Graph():
    
    """
    Graph Data Structure
    
        Protected Variables:
            _vertices: Set[Node]: Set of Vertices
            _edges:List[Tuple[Node,Node]]: List of edges of graph, where each edge is a Node,Node pair
  
    """



    def __init__(self,vertices:Iterable[Node],edges:List[Tuple[Node,Node]]):
        
        """
        Constructor:
        Params:
            vertices:Iterable[Node] -> List of nodes of graph, duplicate nodes will be eliminated
            edges:List[Tuple[Node,Node]] -> List of node pairs, representing the edges of graph

        Raises Exception When:
            An node of an edge doesn't exist in node set
            
            """
        
        self._vertices:Set[Node] = set(vertices)
        self._edges:List[Tuple[Node,Node]]=[]

        for edge in self._edges:
            
            if not(edge[0] in self._vertices and edge[1] in self._vertices):
                raise Exception("An End Point of Edge Doesnt Exist in Vertice Set")
            
            self._edges.append(edge)



    def _create_adjacency_matrix(self)->None:
        
        """
        A function to create adjacency matrix representation of graph.

        _adjacency_matrix: np.ndarray[int]

        """





        pass
    

    
