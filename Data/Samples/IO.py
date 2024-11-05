import Graph
import fnmatch


def read_graph(file_path: str) -> Graph.Graph():
    """
    A function to read graph from a file and return a graph object.
    Supports GraphML Format
    Params:
        file_path:str -> path to file containing graph data
    Returns:
        g:Graph -> graph object constructed from file data
    """

    if fnmatch.fnmatch(file_path, "*.graphml"):

        g = Graph.Graph()
        g.read_graphml(file_path)
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