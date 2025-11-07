import time
import numpy as np
import math
from itertools import permutations

def read_file(file):
    dimension = 1
    matrix = []

    with open(file) as obj:
        data = obj.readlines()
    obj.close()


    isMatrix = False
    i = 0
    j = 0
    for line in data:

        if isMatrix:
            value = int(line.strip('\n'))
            if i != j:
                matrix[i][j] = value
                matrix[j][i] = value
                i += 1
            else:
                j += 1
                i = 0

        if line.startswith("DIMENSION"):
            text = line
            text = text[text.index(':')+1:]
            text.strip(' ')
            text.strip('\n')
            dimension = int(text)
            matrix = np.zeros([dimension,dimension],dtype='int')

        if line.startswith("EDGE_WEIGHT_SECTION"):
            isMatrix = True

        if i == 25 and j == 25:
            isMatrix = False

    return dimension, matrix


def tsp(matrix, start):

    vertex = list(range(1,27))
    vertex.remove(start)

    p = permutations(vertex)
    routes = []
    for i,r in enumerate(p):
        print(i)
        routes.append(r)

    minimum = 257*26
    print(1)
    mini_route = ()
    for i, r in enumerate(routes):
        distance = matrix[0][r[0]]
        for j in range(0,len(r)-1):

            distance += matrix[r[j]][r[j+1]]

        distance += matrix[r[24]][0]
        if distance < minimum:
            minimum = distance
            mini_route = list(r)
        
        print(mini_route)
 
    

    print(mini_route)
    return mini_route

def minimum_distanse(vertex, matrix):

    l = vertex
    minimum = 0

    if len(vertex) == 1:
        minimum = matrix[0,vertex[0]-1]
    else:
        for k in vertex:
            l = list(vertex)
            l.remove(k)

            p = permutations(l)
            for i,r in enumerate(p):


                
                minimum = minimum + minimum_distanse(l, matrix)




def tsp2(novisited, end_vertex, matrix, temp):

    minimum_distance = 257*26
    route = []

    if len(novisited) == 0:
        return route, matrix[0][end_vertex-1]
    
    for item in enumerate(temp[end_vertex]):
        if item[1][0] == novisited:
            return item[1][1],item[1][2]
    
    for vertex in novisited:  

        remain_vertex = novisited.copy()
        remain_vertex.remove(vertex)
        tsp_route, tsp_distance = tsp2(remain_vertex, vertex, matrix, temp)
        tsp_route_copy = tsp_route.copy()
        tsp_route_copy.append(vertex)
        distanse = tsp_distance + matrix[vertex-1][end_vertex-1]

        if distanse < minimum_distance:
            route = tsp_route_copy
            minimum_distance = distanse

    temp[end_vertex].append([novisited,route,minimum_distance])
    
    return route, minimum_distance




if __name__=="__main__":

    file = "fri26.tsp"

    try:
        dimension, matrix = read_file(file)


        b = 1
        route = []
        start = time.time()

        all_vertex = list(range(2,6))
        temp={}
        for i in range(1,27):
            temp[i] = []
        route, dimension = tsp2(all_vertex, 1, matrix, temp)
        print(temp)
        end = time.time()
        print("執行時間:",end-start,"秒")

        print(route)
        #route = [1,2,3,4,6,5,7,8,9,10,14,15,13,12,11,16,19,20,18,17,21,22,26,23,24,25,1]

        sum = 0
        for i in range(len(route)-1):
            sum = sum + matrix[route[i]-1][route[i+1]-1]

        print(sum)

    except Exception as e:
        print(e)
    



