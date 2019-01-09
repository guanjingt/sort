import math



class heapsort():

    def __init__(self):
        self.array = [2,6,9,23,14,25,13,94,37,7,8]
        self._heap_size = len(self.array)

    def parent(self, i):
        return math.floor(i/2)

    def left(self, i):
        return math.floor(2*i+1)

    def right(self, i):
        return math.floor(2*i+2)

    def max_heapify(self, A, i):
        l = self.left(i)
        r = self.right(i)

        if l< self._heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r< self._heap_size and A[r] >A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)

    def build_max_heap(self, A):
        for i in range(math.ceil(len(A)/2), -1, -1):
            self.max_heapify(A, i)
        return A

    def heapsort(self, A):
        self.build_max_heap(A)
        for i in range(len(A)-1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self._heap_size -= 1
            self.max_heapify(A, 0)
        return A

    def run(self):
        tem = self.heapsort(self.array)
        print(tem)



if __name__ == '__main__':
    object = heapsort()
    object.run()
