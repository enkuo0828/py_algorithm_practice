class BaseAlgorithm:

    def __init__(self, arr):
        self.step_count = 0
        self.result = self.main(arr)

    def swap(self, x, y):
        temp = None
        temp = x
        x = y
        y = temp
        return x, y

    def main(self):
        raise NotImplementedError
