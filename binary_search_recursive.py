def binarySearch(A, low, high, key):
    if low == high:
        if A[low] == key:
            return low
        else:
            return 0
    else:
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        if A[mid] < key:
            return binarySearch(A, mid + 1, high, key)
        else:
            return binarySearch(A, low, mid - 1, key)

def main():
    A = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
    low = 1
    high = len(A)
    key = int(input("Please enter a key number: "))
    result = binarySearch(A,low, high, key)
    if result == 0:
        print("Key nout found!")
    else:
        print("%d is located at position %d" % (key, result))

if __name__ == "__main__":
    main()
