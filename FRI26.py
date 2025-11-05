import time
import numpy as np

def read_file(file):
    start = time.time()
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

    end = time.time()
    print("執行時間:",end-start,"秒")

    return dimension, matrix







if __name__=="__main__":

    file = "fri26.tsp"

    try:
        dimension, matrix = read_file(file)

    except Exception as e:
        print(e)
    



