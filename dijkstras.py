import heapq

def dijkstra(graph, start):
    # Initialise distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the new distance is shorter, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def get_shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current != start:
        if current is None:
            return []  # No path
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
    return path[::-1]

# Sample graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 1},
    'E': {'D': 1}
}

# Dijkstra's algorithm
start_node = 'A'
end_node = 'E'
distances, previous_nodes = dijkstra(graph, start_node)
shortest_path = get_shortest_path(previous_nodes, start_node, end_node)

# Output
print("Shortest distances from node A:")
for node, dist in distances.items():
    print(f"Distance to {node}: {dist}")

print(f"\nShortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
