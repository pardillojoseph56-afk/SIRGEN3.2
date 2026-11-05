# Algorithm StackName: push each letter, then pop until empty (LIFO).

def main():
    name = input("Enter a name (press Enter for PARDILLO): ").strip().upper() or "PARDILLO"

    stack = [None] * len(name)   # DECLARE stack[n]
    top = -1

    # PUSH each letter
    for letter in name:
        top += 1
        stack[top] = letter
        print("Pushed:", letter)

    # POP until empty
    while top != -1:
        print("Popped:", stack[top])
        top -= 1

    print("Stack is empty")


if __name__ == "__main__":
    main()
