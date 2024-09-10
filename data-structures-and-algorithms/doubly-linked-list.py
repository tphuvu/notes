class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # In danh sách liên kết đôi
    def print_list(self):
        if not self.head:
            print("Danh sách rỗng")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

    # Thêm node vào cuối danh sách
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Thêm node vào đầu danh sách
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Thêm node sau một node cụ thể
    def add_after(self, target_data, data):
        temp = self.head
        while temp:
            if temp.data == target_data:
                new_node = Node(data)
                new_node.next = temp.next
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                new_node.prev = temp
                return
            temp = temp.next
        print(f"Node {target_data} không tồn tại trong danh sách")

    # Thêm node trước một node cụ thể
    def add_before(self, target_data, data):
        temp = self.head
        while temp:
            if temp.data == target_data:
                new_node = Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev:
                    temp.prev.next = new_node
                else:
                    self.head = new_node
                temp.prev = new_node
                return
            temp = temp.next
        print(f"Node {target_data} không tồn tại trong danh sách")

    # Xóa node
    def delete(self, target_data):
        temp = self.head

        # Trường hợp danh sách rỗng
        if not temp:
            print("Danh sách rỗng")
            return

        # Trường hợp chỉ có một node
        if temp.next is None and temp.data == target_data:
            self.head = None
            return

        # Trường hợp xóa node đầu
        if temp.data == target_data:
            self.head = temp.next
            self.head.prev = None
            return

        # Trường hợp xóa node ở giữa hoặc cuối
        while temp:
            if temp.data == target_data:
                if temp.next:  # Node ở giữa
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:  # Node ở cuối
                    temp.prev.next = None
                return
            temp = temp.next

        print(f"Node {target_data} không tồn tại trong danh sách")

    # Đảo ngược danh sách liên kết đôi
    def reverse(self):
        temp = self.head
        if not temp:
            return

        while temp:
            temp.prev, temp.next = temp.next, temp.prev  # Đảo ngược con trỏ prev và next
            if not temp.prev:  # Sau khi đảo ngược, temp.prev sẽ là None khi ở node cuối
                self.head = temp  # Cập nhật lại head
            temp = temp.prev  # Tiếp tục đảo ngược đến node tiếp theo


# Ví dụ sử dụng
dll = DoublyLinkedList()

# Thêm một số phần tử vào danh sách
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(0)

# In danh sách
print("Danh sách liên kết đôi ban đầu:")
dll.print_list()

# Thêm node sau node có giá trị 20
dll.add_after(20, 25)
print("\nSau khi thêm 25 sau 20:")
dll.print_list()

# Thêm node trước node có giá trị 10
dll.add_before(10, 5)
print("\nSau khi thêm 5 trước 10:")
dll.print_list()

# Xóa node đầu tiên
dll.delete(0)
print("\nSau khi xóa node đầu (0):")
dll.print_list()

# Xóa node cuối cùng
dll.delete(30)
print("\nSau khi xóa node cuối (30):")
dll.print_list()

# Đảo ngược danh sách
dll.reverse()
print("\nSau khi đảo ngược danh sách:")
dll.print_list()
