import numpy as np

items = [{'value': np.random.randint(10, 90)} for _ in range(100)]

def initializeSolution():
    return [np.random.choice([0, 1]) for _ in range(100)]

def knapsack_optimizer(number_of_iterations):
    bestSolution = initializeSolution()
    best_total_value = computeTotalValue(bestSolution)
    print("Items array:")
    print(items)
    print("\nInitial solution:")
    print(bestSolution)
    print(f"\nInitial Total Value: {best_total_value}")
    for iteration in range(1, number_of_iterations + 1):
        newSolution = modifySolution(bestSolution)
        new_total_value = computeTotalValue(newSolution)
        if new_total_value > best_total_value:
            bestSolution = newSolution
            best_total_value = new_total_value
            print(f"\nIteration {iteration}:")
            print("Solution:")
            print(bestSolution)
            print(f"Total Value: {new_total_value}")
    return bestSolution, best_total_value

def modifySolution(solution):
    index = np.random.randint(0, 99)
    solution[index] = 1 - solution[index]  
    return solution.copy()

def computeTotalValue(solution):
    total_value = 0
    total_weight = 0
    for i in range(100):
        if solution[i] == 1:
            total_value += items[i]['value']
            total_weight += 1
    if total_weight > 2500:
        return 0 
    return total_value

best_solution, best_total_value = knapsack_optimizer(5000)

print("\nBest solution:")
print(best_solution)
print("Best total value:", best_total_value)