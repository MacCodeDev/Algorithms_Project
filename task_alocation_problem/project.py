import numpy as np 

processor_list = [{'delay': 1}, {'delay': 2} , {'delay': 3}, {'delay': 4}] 
task_list = np.random.randint(10, 90, size=100) 

def evaluate_distribution(task_distribution): 
    total_time = 0 
    for i in range(100): 
        total_time += task_list[i] * processor_list[task_distribution[i]]['delay'] 
    return total_time 

def create_random_distribution(): 
    return np.random.choice([i for i in range(4)], size=100) 

def modify_distribution(distribution): 
    index = np.random.randint(0, 99) 
    distribution[index] = np.random.choice([i for i in range(4)]) 
    return distribution.copy() 

def run_genetic_algorithm(num_generations): 
    optimal_distribution = create_random_distribution() 
    optimal_evaluation = evaluate_distribution(optimal_distribution) 

    print("Array of tasks with their execution times:") 
    print(task_list) 
    print("\nInitial allocation of tasks to processors:") 
    print(optimal_distribution) 
    print(f"\nInitial total execution time: {optimal_evaluation}") 

    for generation in range(1, num_generations + 1): 
        new_distribution = modify_distribution(optimal_distribution) 
        new_evaluation = evaluate_distribution(new_distribution) 

        if new_evaluation < optimal_evaluation: 
            optimal_distribution = new_distribution 
            optimal_evaluation = new_evaluation 

            print(f"\nAfter mutation {generation}:") 
            print("New allocation of tasks to processors:") 
            print(optimal_distribution) 
            print(f"New total execution time: {new_evaluation}") 

    return optimal_distribution, optimal_evaluation 

optimal_distribution, optimal_evaluation = run_genetic_algorithm(5000) 

print("\nBest allocation of tasks to processors:") 
print(optimal_distribution) 
print("Minimum total execution time:", optimal_evaluation)