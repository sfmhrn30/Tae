def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k    
    return m, s
def print_optimal_parentheses(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parentheses(s, i, s[i][j])
        print_optimal_parentheses(s, s[i][j] + 1, j)
        print(")", end="")
def generate_all_parenthesizations(matrix_dimensions):
    n = len(matrix_dimensions) - 1
    results = []

    def generate(i, j):
        if i == j:
            return [f"A{i + 1}"]
        parenthesizations = []
        for k in range(i, j):
            left = generate(i, k)
            right = generate(k + 1, j)
            for l in left:
                for r in right:
                    parenthesizations.append(f"({l} * {r})")
        return parenthesizations
    all_parenthesizations = generate(0, n - 1)
    for parenthesization in all_parenthesizations:
        cost = calculate_cost(parenthesization, matrix_dimensions)
        results.append((parenthesization, cost))
    return results


def calculate_cost(parenthesization, matrix_dimensions):
    stack = []
    cost = 0

    for symbol in parenthesization:
        if symbol.isnumeric():
            stack.append([int(symbol),matrix_dimensions[int(symbol)-1],matrix_dimensions[int(symbol)]])
        elif symbol == '*':
            continue
        elif symbol == ')':
            right = stack.pop()
            left = stack.pop()
            cost += left[1]*left[2]*right[2]
            stack.append([left[0],left[1],right[2]])
    return cost

matrix_dimensions = [40,20,30,10,30]
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of multiplications:", m[1][-1])
print("Optimal parenthesization: ", end="\n")
print_optimal_parentheses(s, 1, len(matrix_dimensions) - 1)
print()
all_parenthesizations = generate_all_parenthesizations(matrix_dimensions)
for parenthesization, cost in all_parenthesizations:
    print("Parenthesization:", parenthesization,end=" : ")
    print("Cost:", cost)
