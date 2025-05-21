import heapq

def a_star(graph, heuristics, start, goal):
    open_set = [(heuristics[start], 0, start, [start])]
    visited = set()

    while open_set:
        estimated_total, current_cost, current_node, path = heapq.heappop(open_set)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            return path, current_cost

        for neighbor, cost in graph[current_node].items():
            if neighbor not in visited:
                g = current_cost + cost
                f = g + heuristics[neighbor]
                heapq.heappush(open_set, (f, g, neighbor, path + [neighbor]))

    return None, float('inf')

# Sample graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Heuristics to goal 'E'
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

start_node = 'A'
goal_node = 'E'

path, total_cost = a_star(graph, heuristics, start_node, goal_node)

if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {total_cost}")
else:
    print("No path found.")
