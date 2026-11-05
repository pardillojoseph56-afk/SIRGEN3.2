# Algorithm ArrayName: add each letter of a name to an array, then remove from the last index.

def main():
    name = input("Enter a name (press Enter for PARDILLO): ").strip().upper() or "PARDILLO"

    arr = [None] * len(name)   # DECLARE arr[n]
    size = 0

    # ADD
    for i in range(len(name)):
        arr[size] = name[i]
        size += 1
    print("Array after adding:", arr)

    # REMOVE (from the last index)
    while size > 0:
        print("Removed:", arr[size - 1])
        arr[size - 1] = None
        size -= 1

    print("Array is empty")


if __name__ == "__main__":
    main()
