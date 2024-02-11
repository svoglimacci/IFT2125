import math
import sys
INFINITY = math.inf
import time
class Edge:
    def __init__(self, w=INFINITY, to=-1):
        self.w = w
        self.to = to



def read_problems(input_file):
    with open(input_file, "r") as file:
        content = file.read()

    lines = content.split('\n')
    return lines

def write(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def prim(adj):
    n = len(adj)
    total_weight = 0
    selected = [False] * n
    min_e = [Edge() for _ in range(n)]
    min_e[0].w = 0

    for _ in range(n):
        v = -1
        for j in range(n):
            if not selected[j] and (v == -1 or min_e[j].w < min_e[v].w):
                v = j

        if min_e[v].w == INFINITY:
            exit(0)

        selected[v] = True
        total_weight += min_e[v].w

        for to in range(n):
            if adj[v][to] < min_e[to].w:
                min_e[to] = Edge(adj[v][to], v)

    end = time.time()
    return total_weight

def main(args):
    input_file = args[0]
    output_file = args[1]

    content = read_problems(input_file)
    num_problems = int(content[0])

    result = ""
    current_line = 1

    for _ in range(num_problems):
        m = int(content[current_line])
        current_line += 1

        coordinates = [tuple(map(float, line.split())) for line in content[current_line:current_line+m]]
        current_line += m

        graph = [[INFINITY] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                distance = calculate_distance(coordinates[i], coordinates[j])
                graph[i][j] = distance
                graph[j][i] = distance


        weight = prim(graph)

        result += f"{weight:.3f}\n"


    write(output_file, result)

if __name__ == '__main__':
    main(sys.argv[1:])
