from .utils import BaseAlgorithm

class InsertionSort(BaseAlgorithm):

    def main(self, arr):
        length = len(arr)
        res = []
        for x in range(1, length):
            temp = arr[x]
            i = x - 1
            while i >= 0 and arr[i] > temp:
                self.step_count += 1
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = temp
        print(self.step_count)
        print(len(arr))
        return arr
