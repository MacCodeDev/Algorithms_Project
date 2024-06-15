import numpy as np
import random

num_cities = 100
cost_matrix = np.random.randint(10, 90, size=(num_cities, num_cities))
np.fill_diagonal(cost_matrix, 0)

def total_cost(tour):
    return sum(cost_matrix[tour[i-1]][tour[i]] for i in range(num_cities))

def mutate_tour(tour):
    new_tour = tour[:]
    i, j = random.sample(range(num_cities), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def evolutionary_strategy(population, num_generations, mutation_rate):
    all_tours = []
    for _ in range(num_generations):
        new_population = []
        for tour in population:
            if random.random() < mutation_rate:
                new_tour = mutate_tour(tour)
                new_population.append(new_tour)
                all_tours.append((new_tour, total_cost(new_tour)))
            else:
                new_population.append(tour)
                all_tours.append((tour, total_cost(tour)))
        population = sorted(new_population, key=total_cost)
    return all_tours, population[0], total_cost(population[0])

initial_population = [random.sample(range(num_cities), num_cities) for _ in range(100)]
num_generations = 100
mutation_rate = 0.1

all_tours, best_tour, best_cost = evolutionary_strategy(initial_population, num_generations, mutation_rate)

for i, (tour, cost) in enumerate(all_tours):
    print(f"Attempt {i+1}: Tour: {tour}, Cost: {cost}")

print("\nBest tour:", best_tour)
print("Best cost:", best_cost)