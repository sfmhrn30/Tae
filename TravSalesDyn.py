def finding_least_path(graph, visited_city, current_position, no_of_cities, count, cost, cycle):
    if no_of_cities == count and graph[current_position][0] > 0:
        cycle = min(cycle, cost + graph[current_position][0])
        return cycle
    for i in range(no_of_cities):
        if not visited_city[i] and graph[current_position][i] > 0:
            visited_city[i] = True
            cycle = finding_least_path(graph, visited_city, i, no_of_cities, count + 1, cost + graph[current_position][i], cycle)
            visited_city[i] = False
    return cycle

def main():
    print("Enter number of Cities: ")
    no_of_cities = int(input())
    graph = [[0] * no_of_cities for _ in range(no_of_cities)]
    
    for i in range(no_of_cities):
        for j in range(no_of_cities):
            print(f"Enter Distance from City {i + 1} to City {j + 1}: ", end="")
            graph[i][j] = int(input())
    
    visited_city = [False] * no_of_cities
    visited_city[0] = True
    cycle = float('inf')

    cycle = finding_least_path(graph, visited_city, 0, no_of_cities, 1, 0, cycle)
    print(cycle)

if __name__ == "__main__":
    main()
