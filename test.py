class Node:
    def __init__(self, data):
        self.data = data  # Lưu trữ dữ liệu
        self.next = None  # Con trỏ trỏ đến node tiếp theo (ban đầu là None)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Khởi tạo danh sách với head là None (danh sách trống)

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
    
    # Phương thức insert_after_node: Chèn phần tử sau một node cụ thể
    def insert_after_node(self, prev_node_data, data):
        current_node = self.head
        while current_node:  # Duyệt qua danh sách
            if current_node.data == prev_node_data:  # Tìm node đích
                new_node = Node(data)  # Tạo node mới
                new_node.next = current_node.next  # Con trỏ của node mới trỏ đến node tiếp theo của node đích
                current_node.next = new_node  # Cập nhật con trỏ của node đích trỏ đến node mới
                return
            current_node = current_node.next
        print(f"Node với giá trị {prev_node_data} không tồn tại trong danh sách liên kết.")


# Sử dụng danh sách liên kết
sll = SinglyLinkedList()

# Thêm các phần tử vào danh sách
sll.append("A")
sll.append("B")
sll.append("C")

# Chèn phần tử sau node "B"
sll.insert_after_node("B", "D")

# Hiển thị danh sách
sll.display() # Output: A -> B -> D -> C -> None

# Chèn phần tử sau node "F"
sll.insert_after_node("F", "D") # Output: Node với giá trị F không tồn tại trong danh sách liên kết.