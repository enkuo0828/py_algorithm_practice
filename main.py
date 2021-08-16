from random import SystemRandom
from sorting.bubble import BubbleSort
from sorting.insertion import InsertionSort

def main():
    r = SystemRandom()
    arr = [r.randint(0,100) for i in range(100)]
    print(InsertionSort(arr).result)


if __name__ == "__main__":
    main()