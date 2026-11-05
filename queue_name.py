# Algorithm QueueName: enqueue each letter, then dequeue until empty (FIFO).

def main():
    name = input("Enter a name (press Enter for PARDILLO): ").strip().upper() or "PARDILLO"

    queue = [None] * len(name)   # DECLARE queue[n]
    front = 0
    rear = -1

    # ENQUEUE each letter
    for letter in name:
        rear += 1
        queue[rear] = letter
        print("Enqueued:", letter)

    # DEQUEUE until empty
    while front <= rear:
        print("Dequeued:", queue[front])
        front += 1

    print("Queue is empty")


if __name__ == "__main__":
    main()
