class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head
        if self.head:
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("(head)")
        else:
            print("List is empty.")

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                current = self.head
                while current.next != self.head:
                    current = current.next
                if self.head == self.head.next:  # Only one element
                    self.head = None
                else:
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next != self.head:
                    prev = current
                    current = current.next
                    if current.data == key:
                        prev.next = current.next
                        break
    # Function to find the length of the Circular Linked List

    def length(self):
        if not self.head:
            return 0
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    # Function to split the Circular Linked List around the midpoint
    def split(self):
        if not self.head:
            return None, None

        length = self.length()
        if length == 1:
            return self, None  # Only one node, no split

        mid = length // 2
        current = self.head
        prev = None

        # Traverse till the midpoint
        for _ in range(mid):
            prev = current
            current = current.next

        # Create the second circular linked list
        second_list = CircularLinkedList()
        second_list.head = current

        # Break the first list
        prev.next = self.head  # Make the first list circular again

        # Traverse the second list to make it circular
        temp = second_list.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = second_list.head

        return self, second_list


# Ví dụ sử dụng
cll = CircularLinkedList()
for i in range(1, 11):
    cll.append(i)

print("Danh sách liên kết vòng ban đầu:")
cll.print_list()

list1, list2 = cll.split()

print("\nDanh sách liên kết vòng thứ nhất:")
list1.print_list()

print("\nDanh sách liên kết vòng thứ hai:")
list2.print_list()
