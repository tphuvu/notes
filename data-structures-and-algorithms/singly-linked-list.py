class Node:
    def __init__(self, data):
        self.data = data  # Lưu trữ dữ liệu
        self.next = None  # Con trỏ trỏ đến node tiếp theo (ban đầu là None)


class SinglyLinkedList:
    def __init__(self):
        # Khởi tạo danh sách với head là None (danh sách trống)
        self.head = None

    # Phương thức append: Chèn một phần tử mới vào cuối danh sách
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Nếu danh sách rỗng, head sẽ là node mới
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Tìm node cuối cùng
            last_node = last_node.next
        last_node.next = new_node  # Gắn node mới vào cuối danh sách

    def prepend(self, data):
        new_node = Node(data)  # Tạo node mới
        new_node.next = self.head  # Con trỏ của node mới trỏ đến node đầu hiện tại
        self.head = new_node  # Cập nhật head để trỏ đến node mới

    def insert_after_node(self, prev_node_data, data):
        current_node = self.head
        while current_node:  # Duyệt qua danh sách
            if current_node.data == prev_node_data:  # Tìm node đích
                new_node = Node(data)  # Tạo node mới
                # Con trỏ của node mới trỏ đến node tiếp theo của node đích
                new_node.next = current_node.next
                current_node.next = new_node  # Cập nhật con trỏ của node đích trỏ đến node mới
                return
            current_node = current_node.next
        print(
            f"Node với giá trị {prev_node_data} không tồn tại trong danh sách liên kết.")

    def insert_at_position(self, position, data):
        new_node = Node(data)

        # Trường hợp vị trí là 0 (chèn vào đầu danh sách)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Trường hợp chèn vào vị trí bất kỳ khác
        current_node = self.head
        count = 0
        prev_node = None

        # Duyệt qua danh sách để tìm vị trí cần chèn
        while current_node and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        # Nếu vị trí vượt quá kích thước của danh sách
        if count != position:
            print(f"Vị trí {position} vượt quá kích thước của danh sách.")
            return

        # Chèn node mới vào vị trí đã tìm thấy
        new_node.next = current_node
        prev_node.next = new_node

    # Phương thức delete_node: Xóa node có dữ liệu cụ thể
    def delete_node(self, key):
        current_node = self.head

    # Trường hợp node cần xóa là head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

    # Trường hợp node cần xóa không phải là head
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

    # Nếu node cần xóa không tồn tại trong danh sách
        if current_node is None:
            print(
                f"Node với giá trị {key} không tồn tại trong danh sách liên kết.")
            return

    # Cập nhật con trỏ của node trước trỏ đến node tiếp theo của node bị xóa
        prev_node.next = current_node.next
        current_node = None

    def delete_at_position(self, position):
        if self.head is None:
            print("Danh sách trống.")
            return

        current_node = self.head

        # Trường hợp node cần xóa ở vị trí 0 (node đầu tiên)
        if position == 0:
            self.head = current_node.next  # Cập nhật head để trỏ đến node tiếp theo
            current_node = None
            return

        # Trường hợp node cần xóa không phải ở vị trí 0
        prev_node = None
        count = 0

        # Duyệt qua danh sách đến vị trí cần xóa
        while current_node and count != position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        # Nếu vị trí không tồn tại trong danh sách
        if current_node is None:
            print(f"Vị trí {position} vượt quá kích thước của danh sách.")
            return

        # Cập nhật con trỏ của node trước trỏ đến node tiếp theo của node bị xóa
        prev_node.next = current_node.next
        current_node = None

        # Phương thức display: In ra các phần tử trong danh sách
    def display(self):
        current_node = self.head
        while current_node:  # Duyệt qua danh sách cho đến khi gặp None
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Sử dụng danh sách liên kết
llist = SinglyLinkedList()

# Thêm các phần tử vào danh sách
llist.append("B")
llist.append("C")
llist.append("E")
# Sử dụng prepend để thêm A vào đầu danh sách
llist.prepend("A")
# Chèn phần tử "D" sau node có giá trị "C"
llist.insert_after_node("C", "D")

# Hiển thị danh sách ban đầu
print("------------------------------\nDanh sách ban đầu:")
llist.display()

# Xóa node tại vị trí 0 (head)
llist.delete_at_position(0)

# Hiển thị danh sách sau khi xóa node tại vị trí 0
print("\nDanh sách sau khi xóa vị trí 0 (head):")
llist.display()

# Xóa node tại vị trí 2
llist.delete_at_position(2)

# Hiển thị danh sách sau khi xóa node tại vị trí 2
print("\nDanh sách sau khi xóa vị trí 2:")
llist.display()

# Xóa node "C" (không phải head)
llist.delete_node("C")

# Hiển thị danh sách sau khi xóa
print("\nDanh sách sau khi xóa C:")
llist.display()

# Xóa node "B" (là head)
llist.delete_node("B")

# Hiển thị danh sách sau khi xóa
print("\nDanh sách sau khi xóa B (head):")
llist.display()

llist.insert_at_position(0, "A")
llist.insert_at_position(1, "B")
llist.insert_at_position(2, "C")
llist.insert_at_position(3, "D")

# Hiển thị danh sách sau khi chèn A, B, C, D

print("\nDanh sách sau khi chèn A, B, C, D:")
llist.display()
