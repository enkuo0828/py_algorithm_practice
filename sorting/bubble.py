from .utils import BaseAlgorithm

class BubbleSort(BaseAlgorithm):
    def __init__(self, arr):
        self.temp_arr = arr
        self.result = []
        self.step_count = 0
        super().__init__(arr)

    def main(self, arr):
        end = len(arr)
        self.step(arr)
        for k in range(end - 1):
            for j in reversed(range(k + 1, end)):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = self.swap(arr[j], arr[j - 1])
                    self.step_count += 1
        print(self.step_count)
        return arr

    def step(self, arr):
        pass
