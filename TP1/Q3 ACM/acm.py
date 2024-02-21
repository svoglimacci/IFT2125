#Nom, Matricule
#Nom, Matricule

import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies
def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines()
    file.close()
    return lines

def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2);

# based on https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
def prim(graph):
    n = len(graph)
    total = 0;
    visited = [False] * n
    edges = [INFINITY] * n
    edges[0] = 0

    for _ in range(n):
        vertex = -1
        for i in range(n):
            if not visited[i] and (vertex == -1 or edges[i] < edges[vertex]):
                vertex = i

        if edges[vertex] == INFINITY:
            return INFINITY

        visited[vertex] = True
        total += edges[vertex]

        for i in range(n):
            if graph[vertex][i] < edges[i]:
                edges[i] = graph[vertex][i]

    return total


#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]

    problems = read_problems(input_file)
    count = int(problems[0])
    result = ""
    curr = 1

    for _ in range(count):
        n = int(problems[curr])
        curr += 1

        coords = []

        for _ in range(n):
            coords.append(tuple(map(float, problems[curr].split())))
            curr += 1

        graph = [[INFINITY] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                distance = euclidean_distance(coords[i], coords[j])
                graph[i][j] = distance
                graph[j][i] = distance

        weight = prim(graph)

        result += f"{weight:.3f}\n"


    write(output_file, result)

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
