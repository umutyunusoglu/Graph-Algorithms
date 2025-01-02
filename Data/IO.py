from .Graph import Graph,Vertex,Edge
import fnmatch
from xml.dom import minidom

def read_graph(file_path: str,directed=False) ->Graph:
    """
    A function to read graph from a file and return a graph object.
    Supports GraphML Format
    Params:
        file_path:str -> path to file containing graph data
    Returns:
        g:Graph -> graph object constructed from file data
    """

    if fnmatch.fnmatch(file_path, "*.graphml"):

        g = _process_graph_ml(file_path,directed)

        return g

    else:
        raise Exception("File Format Not Supported")


def _process_graph_ml(file_path: str,directed=False) -> Graph:
    """
    A helper function to read and process graphml file to a graph object.

    Params:
        file_path:str -> path to file containing graph data
    Returns:
        g:Graph -> graph object constructed from file data
    """
    dom = minidom.parse(file_path)


    raw_v = dom.getElementsByTagName('node')
    raw_e=dom.getElementsByTagName('edge')

    vertices=[]
    edges=[]
    for v in raw_v:

        v_data={}
        data=v.getElementsByTagName("data")
        
        
        for d in data:
            v_data[d.getAttribute("key")]=d.firstChild.nodeValue
        

        vertices.append(Vertex(v_id=int(v.attributes['id'].value),value=v_data))
    
    for e in raw_e:

        source=int(e.getAttribute("source"))
        target=int(e.getAttribute("target"))

        edges.append(Edge(source,target,directed))
    
         
    return Graph(vertices,edges)



if(__name__=="__main__"):

    g=read_graph("../airlines.graphml")

    for row in g._adjacency_matrix:
        for i in row:
            if(i==1):
                print(row)
                break