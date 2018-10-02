import sys

def quicksort(unsortedArray):
    if len(unsortedArray) == 1 or len(unsortedArray) == 0:
        return unsortedArray
    pivot = unsortedArray[-1]
    wall = 0
    for i in range(len(unsortedArray) - 1):
        if unsortedArray[i] <= pivot:
            unsortedArray[wall], unsortedArray[i] = unsortedArray[i], unsortedArray[wall]
            wall += 1

    unsortedArray[wall], unsortedArray[-1] = unsortedArray[-1], unsortedArray[wall]
    return quicksort(unsortedArray[0:wall]) + [unsortedArray[wall]] + quicksort(unsortedArray[wall+1:])

if __name__ == "__main__":
    unsortedArray = sys.argv[1].split(',')
    unsortedArray = list(map(int, unsortedArray))
    print quicksort(unsortedArray)
