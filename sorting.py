class mySort(object):

    def Bubblesort(self, A):
        for i in range(len(A)):
            for k in range(len(A) - 1, i, -1):
                if (A[k] < A[k - 1]):
                    self.swap(A, k, k - 1)

    def RBubblesort(self, A):
        for i in range(len(A)):
            for k in range(len(A) - 1, i, -1):
                if (A[k] > A[k - 1]):
                    self.swap(A, k, k - 1)

    def insertionsort(self, alist):
        for index in range(1, len(alist)):
            currentvalue = alist[index]
            position = index
            while position > 0 and alist[position-1] > currentvalue:
                alist[position] = alist[position-1]
                position = position-1
            alist[position] = currentvalue

    def Rinsertionsort(self, alist):
        for index in range(1, len(alist)):
            currentvalue = alist[index]
            position = index
            while position > 0 and alist[position-1] < currentvalue:
                alist[position] = alist[position-1]
                position = position-1
            alist[position] = currentvalue

    def mergesort(self, int_lst):
        return int_lst.sort()

    def Rmergesort(self, int_lst):
        return int_lst.sort(reverse=True)

    def heapdel(self, alist):
        minval = alist[0]
        largest = len(alist)-1
        alist[0] = alist[largest]
        del alist[0]
        self.heapsort(alist)
        print("deleted Item : ", minval)

    def heapadd(self, alist, val):
        alist.append(val)
        self.heapsort(alist)
        print("Item Added")

    def buildheap(self, aList):
        length = len(aList) - 1
        leastParent = int(length / 2)
        for i in range(leastParent, -1, -1):
            self.minheapify(aList, i, length)

    def heapsort(self, aList):
        length = len(aList) - 1
        self.buildheap(aList)
        for i in range(length, 0, -1):
            if aList[0] > aList[i]:
                self.swap(aList, 0, i)
                self.minheapify(aList, 0, i - 1)

    def minheapify(self, aList, first, last):
        largest = 2 * first + 1
        while largest <= last:
            if (largest < last) and (aList[largest] < aList[largest + 1]):
                largest += 1
            if aList[largest] > aList[first]:
                self.swap(aList, largest, first)
                first = largest
                largest = 2 * first + 1
            else:
                return

    def swap(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
