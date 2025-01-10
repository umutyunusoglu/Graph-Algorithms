# Sugraph

Sugraph is a Python library for working with graphs. It provides efficient implementations of popular graph algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), Ford-Fulkerson, Bellman-Ford, and Dijkstra's algorithm. This library is designed to be easy to use and suitable for educational purposes or real-world applications.

## Features
- **Breadth-First Search (BFS):** Explore graph layers level by level.
- **Depth-First Search (DFS):** Traverse deeper into the graph before backtracking.
- **Ford-Fulkerson Algorithm:** Compute the maximum flow in a flow network.
- **Bellman-Ford Algorithm:** Find the shortest paths from a single source node, including graphs with negative weights.
- **Dijkstra's Algorithm:** Compute the shortest paths from a single source node in graphs with non-negative weights.

## Installation

To install Sugraph, use pip:

```bash
pip install sugraph
```

Alternatively, you can install the library directly from the source:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sugraph.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sugraph
   ```

3. Install the library:

   ```bash
   pip install .
   ```

## Usage

Here's a quick example to demonstrate how to use Sugraph:

### Example 1: Create a graph using vertices and edges

```python
from sugraph.Data import Graph

vertices = [1, 2, 3, 4, 5]
edges = [
    (1, 2, 1),
    (1, 4, 1),
    (2, 3, 1),
    (2, 4, 1),
    (3, 5, 1),
    (4, 5, 1)
]

g = Graph(vertices, edges)
```

### Example 2: Create a graph from an adjacency matrix

```python
adj_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

g = Graph.from_adjacency_matrix(adj_matrix)
```

### Example 3: Perform BFS and Dijkstra's Algorithm

```python
from sugraph.Algorithms.Traversal import BFS
from sugraph.Algorithms.ShortestPath import dijkstra
bfs_result = BFS(g,1,3)
print("BFS Traversal:", bfs_result)

dijkstra_result = dijsktra(g,1,3)
print("Shortest Paths:", dijkstra_result)
```

## Contributing

Contributions are welcome! If you'd like to contribute to Sugraph, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

Sugraph is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/umutyunusoglu/sugraph/blob/main/LICENSE.md) file for details.

---

For any questions or feedback, feel free to open an issue on GitHub or reach out to the project maintainer.

