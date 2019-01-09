


class quick_sort():

    def __init__(self):
        self.array = [2,8,7,1,3,6,4,5,6]


    def partition(self,A,p,r):
        x = A[r]
        i = p-1
        for j in range(p,r,1):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i+1], A[r] = A[r], A[i+1]

        return i+1


    def quicksort(self,A,p,r):
        if p<r:
            q = self.partition(A,p,r)
            self.quicksort(A,p,q-1)
            self.quicksort(A,q+1,r)
        return A



    def run(self):
        result = self.quicksort(self.array,0,len(self.array)-1)

        print (result)


if __name__ == '__main__':
    object = quick_sort()
    object.run()

