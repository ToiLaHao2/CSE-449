# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)  # Print the node if it hasn't been visited yet
        visited.add(node)  # Mark the node as visited
        for neighbour in graph[node]:  # Recur for all the neighbours of the node
            dfs(visited, graph, neighbour)
            
# Drivers code
dfs(visited, graph, 'A')  # Start the DFS from node 'A'