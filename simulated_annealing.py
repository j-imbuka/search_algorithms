import math
import random

# dataset: City coordinates
cities = {
    "A": (0, 0),
    "B": (2, 3),
    "C": (5, 4),
    "D": (1, 8),
    "E": (7, 2),
    "F": (6, 6)
}

# Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Total path length
def total_distance(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(path[i], path[(i + 1) % len(path)])  # Return to start
    return dist

# Simulated Annealing for TSP
def simulated_annealing_tsp(cities, initial_temp, cooling_rate, max_iter):
    city_names = list(cities.keys())
    current_solution = city_names[:]
    random.shuffle(current_solution)
    current_cost = total_distance(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost
    temperature = initial_temp

    for _ in range(max_iter):
        # Generate new neighbor by swapping two cities
        i, j = random.sample(range(len(city_names)), 2)
        neighbor = current_solution[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        neighbor_cost = total_distance(neighbor)
        delta = neighbor_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_solution = neighbor
            current_cost = neighbor_cost

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost

# Run the algorithm
best_path, best_path_cost = simulated_annealing_tsp(
    cities,
    initial_temp=1000,
    cooling_rate=0.995,
    max_iter=5000
)

# Output the result
print("Best path found:", " -> ".join(best_path) + f" -> {best_path[0]}")
print(f"Total distance: {best_path_cost:.2f}")
