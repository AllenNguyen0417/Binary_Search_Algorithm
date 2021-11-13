def binarySearch(A,size,key):

    # Set low = first position of list
    low = 1 

    # Set high = last position of list
    high = size

    while low <= high:
        # Set mid = (low + high) / 2
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        if A[mid] > key:
            high = mid - 1
        else: 
            low = mid + 1
    return 0


def main():
    A = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
    size = len(A)
    key = int(input("Please enter a key number: "))
    result = binarySearch(A,size,key)
    if result == 0:
        print("Key nout found!")
    else:
        print("%d is located at position %d" % (key, result))

if __name__ == "__main__":
    main()
    