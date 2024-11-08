import Graph
import fnmatch
from xml.dom import minidom

def read_graph(file_path: str) -> Graph.Graph:
    """
    A function to read graph from a file and return a graph object.
    Supports GraphML Format
    Params:
        file_path:str -> path to file containing graph data
    Returns:
        g:Graph -> graph object constructed from file data
    """

    if fnmatch.fnmatch(file_path, "*.graphml"):

        g = _process_graph_ml(file_path)

        return g

    else:
        raise Exception("File Format Not Supported")


def _process_graph_ml(file_path: str) -> Graph.Graph:
    """
    A helper function to read and process graphml file to a graph object.

    Params:
        file_path:str -> path to file containing graph data
    Returns:
        g:Graph -> graph object constructed from file data
    """
    g = Graph.Graph()


    return g



if(__name__=="__main__"):

    dom = minidom.parse("./Sample Data/airlines.graphml")
    vertices = dom.getElementsByTagName('node')
    edges=dom.getElementsByTagName('edge')
    print(f"There are {len(vertices)} items:")

    for element in vertices:
   
        data=element.getElementsByTagName("data")
        print("id:",element.attributes['id'].value)
        for d in data:
            
            match d.getAttribute("key"):
                
                case "x":
                    print("x:",d.firstChild.nodeValue)
                    

                case "y":
                    print("y:",d.firstChild.nodeValue)


        print("-------------------------")

    for element in edges:
        print(element.getAttribute("source"),element.getAttribute("target"))