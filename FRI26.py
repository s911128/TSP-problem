import time
import numpy as np

matrix = []

def read_file(file):
    dimension = 1
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

        if i == dimension-1 and j == dimension-1:
            isMatrix = False

    return dimension, matrix



def tsp(novisited, start_vertex, end_vertex):

    minimum_distance = float("inf")
    route = []
    route.append(start_vertex)
    remain_count = len(novisited)

    if len(novisited) == 0:
        return route, matrix[start_vertex-1][end_vertex-1]
    
    for item in enumerate(temp[remain_count][end_vertex]):
        if item[1][0] == novisited:
            return item[1][1],item[1][2]
    
    for vertex in novisited:  

        remain_vertex = novisited.copy()
        remain_vertex.remove(vertex)
        tsp_route, tsp_distance = tsp(remain_vertex, start_vertex, vertex)
        tsp_route_copy = tsp_route.copy()
        tsp_route_copy.append(vertex)
        distanse = tsp_distance + matrix[vertex-1][end_vertex-1]

        if distanse < minimum_distance:
            route = tsp_route_copy
            minimum_distance = distanse

    temp[remain_count][end_vertex].append([novisited,route,minimum_distance])
    
    
    return route, minimum_distance




if __name__=="__main__":

    file = "fri26.tsp"

    try:
        dimension, matrix = read_file(file)

        start_vertex = 1
        end_vertex = 1
        route = []
        temp={}


        start = time.time()
        
        #dimension = 4       #測試用

        all_vertex = list(range(1,dimension+1))
        all_vertex.remove(start_vertex)

        #根據維度建立temp{去掉前一個端點後尚未訪問的端點數量:{前一個端點:[[剩餘未訪問的端點],[距離最短的路徑],[最短的路徑的距離]]}}
        #例:temp{
        #       1:{
        #           2:[[[3], [1, 3], np.int64(133)], [[4], [1, 4], np.int64(182)]]   ##1→3→2:133,1→4→2:182
        #           3:[[[4], [1, 4], np.int64(171)]]                                 ##1→4→3:171
        #       }
        #       2:{
        #           2:[[[4, 5], [1, 5, 4], np.int64(197)]]                           ##1→5→4→2:197
        #       }
        # 
        # 
        #       n-1:{
        #           1:[[[2, 3, 4, 5], [1, 3, 5, 4, 2], np.int64(282)]]               ##1→3→5→4→2→1:282
        #       }
        # }
        for i in range(1,dimension-1):
            temp[i] = {}
            for j in range(2,dimension+1):
                temp[i][j] = []
        temp[dimension-1]= {1:[]}

        #tsp程式
        route, minimum = tsp(all_vertex,start_vertex, end_vertex)

        end = time.time()
        print("執行時間:",end-start,"秒")
        print("最佳解: ", route)
        print("總距離: ", minimum)

        #route = [1,25,24,23,26,22,21,17,18,20,19,16,11,12,13,15,14,10,9,8,7,5,6,4,3,2]

    except Exception as e:
        print(e)
    



