
def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
    
    print("\nMatriz de Adyacencia:")
    for row in matrix:
        print(row)
    return matrix

adj_list = {}
try:
    num_nodes = int(input("How many nodes does the graph have? (e.g., 4): "))

    for i in range(num_nodes):
        user_input = input(f"Enter neighbors for node {i} separated by commas (leave empty if none): ")
        
        if user_input.strip():
            neighbors = [int(n.strip()) for n in user_input.split(",")]
            adj_list[i] = neighbors
        else:
            adj_list[i] = []

    adjacency_list_to_matrix(adj_list)

except ValueError:
    print("Error: Please enter integers only.")