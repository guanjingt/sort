import math
class Solution():

    def Merge(self,A,p,q,r):
        # print (A,p,q,r)
        n1 = q-p+1
        n2 = q-p

        # print ("A",A,type(A),p,q)
        L=A[p:q+1]
        # print ("L",L)
        R=A[q+1:r+1]
        # print ("R",R)

        L.append(100000)
        R.append(100000)

        i = 0
        j = 0

        k = p
        while (k<=r):
            # print ("LR",L[i] ,R[j])

            if (L[i] == R[j]) and (L[i] == 100000):
                break
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[k] = R[j]
                j = j+1
            # print ("one A",k,A)
            k=k+1



    def MergeSort(self,A,p,r):

        if p<r:
            q=math.floor((p+r)/2)
            print ("M:A",A,"p",p,"r",r)
            self.MergeSort(A,p,q)
            self.MergeSort(A,q+1,r)
            self.Merge(A,p,q,r)

    def run(self):
        A=[8,4,5,9,7,1,2,3,6]
        print (A)
        self.MergeSort(A,0,len(A))

        print ("result A",A)

if __name__ == '__main__':
    object = Solution()
    object.run()



