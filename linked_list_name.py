# Algorithm LinkedListName: insert letters at the tail, then delete at the head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    name = input("Enter a name (press Enter for PARDILLO): ").strip().upper() or "PARDILLO"

    head = None

    # ADD (insert at tail)
    for letter in name:
        new_node = Node(letter)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Show the list
    parts = []
    temp = head
    while temp is not None:
        parts.append(temp.data)
        temp = temp.next
    print("Linked list:", " -> ".join(parts) + " -> NULL")

    # REMOVE (delete at head)
    while head is not None:
        print("Removed:", head.data)
        head = head.next

    print("Linked list is empty")


if __name__ == "__main__":
    main()
