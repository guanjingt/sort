import math
import numpy as np

class Bucket_sort():

    def __init__(self):
        self.list1 = [78,17,39,34,26,72,94,21,12,23,68,34]

    def bucketsort(self, A):
        n = len(A)
        B = []
        C = []
        for i in range(10):
            B.append('0')
        for i in range(n):

            #B[math.floor(A[i]/10)] = B[math.floor(A[i]/10)], A[i]
            B[math.floor(A[i]/10)] += " "+str(A[i])
        for i in range(10):
            B[i] = B[i].split(" ")
            B[i] = sorted(B[i])


        for i in range(10):
            length = len(B[i])
            if length == 1:
                continue
            else:
                for j in range(1,length,1):
                    C.append(B[i][j])

        return C

    def run(self):
        result = self.bucketsort(self.list1)
        print (result)
        a = list(map(int, result))
        print (a)
        #print(sorted(self.list1))


if __name__ == '__main__':
    object = Bucket_sort()
    object.run()




