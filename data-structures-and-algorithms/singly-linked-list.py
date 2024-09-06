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

    def get_length_iterative(self):
        count = 0
        current_node = self.head
        while current_node:  # Duyệt qua danh sách cho đến khi gặp None
            count += 1
            current_node = current_node.next
        return count

    # Phương thức tính độ dài recursive
    def get_length_recursive(self, node):
        # Nếu node là None, tức là danh sách rỗng hoặc đến cuối danh sách
        if not node:
            return 0
        # Tính độ dài đệ quy cho các node tiếp theo
        return 1 + self.get_length_recursive(node.next)

    # Phương thức hoán đổi hai node
    def swap_nodes(self, key1, key2):
        # Nếu hai node giống nhau, không cần hoán đổi
        if key1 == key2:
            return

        # Tìm vị trí của key1
        prev_node1 = None
        current_node1 = self.head
        # Vòng lặp while 1: Tìm vị trí của key1
        while current_node1 and current_node1.data != key1:
            prev_node1 = current_node1
            current_node1 = current_node1.next

        # Tìm vị trí của key2
        prev_node2 = None
        current_node2 = self.head
        # Vòng lặp while 2: Tìm vị trí của key2
        while current_node2 and current_node2.data != key2:
            prev_node2 = current_node2
            current_node2 = current_node2.next

        # Nếu không tìm thấy một trong hai node, dừng lại
        if not current_node1 or not current_node2:
            print("Một hoặc cả hai node không tồn tại.")
            return

        # Nếu key1 không phải là head, cập nhật con trỏ của prev_node1
        if prev_node1:
            prev_node1.next = current_node2
        else:  # Nếu key1 là head
            # Cập nhật head để trỏ đến node mới ("D")
            self.head = current_node2

        # Nếu key2 không phải là head, cập nhật con trỏ của prev_node2
        if prev_node2:
            prev_node2.next = current_node1  # "C" --> "A"
        else:  # Nếu key2 là head
            self.head = current_node1

        # Hoán đổi con trỏ next của hai node
        current_node1.next, current_node2.next = current_node2.next, current_node1.next

        # A sẽ trỏ đến None
        # D (self.head) trỏ đến B
        # Còn B vẫn giữ như cũ trỏ đến C, C thì ở trên đã trỏ đến "A"

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Lưu trữ node tiếp theo
            current.next = prev  # Đảo ngược liên kết
            prev = current  # Di chuyển prev lên
            current = next_node  # Di chuyển current lên node tiếp theo
        # Cập nhật head để trỏ đến node cuối cùng (bây giờ là node đầu tiên)
        self.head = prev

    # Phương thức gộp hai danh sách liên kết đã sắp xếp

    def merge_sorted_lists(self, other_list):

        head1 = self.head  # con trỏ tới đầu danh sách 1
        head2 = other_list.head  # con trỏ tới đầu danh sách 2
        tail = None  # theo dõi phần cuối của merged list

        # Kiểm tra nếu danh sách đầu tiên rỗng
        if not head1:
            return head2
        # Kiểm tra nếu danh sách thứ hai rỗng
        if not head2:
            return head1

        # Bắt đầu so sánh giá trị của hai danh sách
        if head1 and head2:
            if head1.data <= head2.data:
                tail = head1
                head1 = tail.next
            else:
                tail = head2
                head2 = tail.next
            new_head = tail  # new_head là con trỏ tới đầu merged list

        # Duyệt qua hai danh sách và tiếp tục so sánh các phần tử
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1  # Kết nối node nhỏ hơn từ head1
                tail = head1
                head1 = tail.next
            else:
                tail.next = head2  # Kết nối node nhỏ hơn từ head2
                tail = head2
                head2 = tail.next

        # Nếu head1 hết node, nối phần còn lại của head2
        if not head1:
            tail.next = head2
        # Nếu head2 hết node, nối phần còn lại của head1
        if not head2:
            tail.next = head1

        self.head = new_head  # Cập nhật lại head của merged list
        return self.head

    # Xóa các phần tử trùng lặp trong danh sách
    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        prev = None
        seen_data = set()  # Tập hợp để lưu các giá trị đã gặp

        while current:
            if current.data in seen_data:  # Nếu giá trị đã gặp
                prev.next = current.next  # Bỏ qua node hiện tại
            else:
                seen_data.add(current.data)  # Thêm giá trị vào tập hợp
                prev = current  # Cập nhật con trỏ prev
            current = current.next  # Di chuyển đến node tiếp theo

    # Tìm node thứ N từ cuối danh sách
    def nth_to_last_node(self, N):
        length = self.get_length_iterative()  # Tính độ dài của danh sách
        if N > length or N <= 0:  # Kiểm tra xem N có hợp lệ không
            return None

        target_index = length - N  # Vị trí tương đương từ đầu danh sách
        current = self.head
        count = 0

        while current:
            if count == target_index:
                return current  # Trả về node thứ N từ cuối
            count += 1
            current = current.next
        return None

    # Phương thức đếm số lần xuất hiện của một giá trị
    def count_occurrences(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    # Phương thức kiểm tra danh sách có phải là palindrome hay không sử dụng List
    def is_palindrome(self):
        values = []
        current = self.head

        # Lưu các giá trị của danh sách liên kết vào một list
        while current:
            values.append(current.data)
            current = current.next

        # Kiểm tra xem list có phải là palindrome không
        return values == values[::-1]

    # Phương thức display: In ra các phần tử trong danh sách
    def display(self):
        current_node = self.head
        while current_node:  # Duyệt qua danh sách cho đến khi gặp None
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# # Sử dụng danh sách liên kết
# llist = SinglyLinkedList()

# # Thêm các phần tử vào danh sách
# llist.append("B")
# llist.append("C")
# llist.append("E")
# # Sử dụng prepend để thêm A vào đầu danh sách
# llist.prepend("A")
# # Chèn phần tử "D" sau node có giá trị "C"
# llist.insert_after_node("C", "D")

# # Hiển thị danh sách ban đầu
# print("------------------------------\nDanh sách ban đầu:")
# llist.display()

# # Xóa node tại vị trí 0 (head)
# llist.delete_at_position(0)

# # Hiển thị danh sách sau khi xóa node tại vị trí 0
# print("\nDanh sách sau khi xóa vị trí 0 (head):")
# llist.display()

# # Xóa node tại vị trí 2
# llist.delete_at_position(2)

# # Hiển thị danh sách sau khi xóa node tại vị trí 2
# print("\nDanh sách sau khi xóa vị trí 2:")
# llist.display()

# # Xóa node "C" (không phải head)
# llist.delete_node("C")

# # Hiển thị danh sách sau khi xóa
# print("\nDanh sách sau khi xóa C:")
# llist.display()

# # Xóa node "B" (là head)
# llist.delete_node("B")

# # Hiển thị danh sách sau khi xóa
# print("\nDanh sách sau khi xóa B (head):")
# llist.display()

# llist.insert_at_position(0, "A")
# llist.insert_at_position(1, "B")
# llist.insert_at_position(2, "C")
# llist.insert_at_position(3, "D")

# # Hiển thị danh sách sau khi chèn A, B, C, D

# print("\nDanh sách sau khi chèn A, B, C, D:")
# llist.display()

# # Tính độ dài bằng phương pháp lặp
# length_iterative = llist.get_length_iterative()
# print(f"\nĐộ dài (lặp): {length_iterative}")

# # Xóa node "E" (không phải head)
# llist.delete_node("E")

# # Hiển thị danh sách sau khi xóa
# print("\nDanh sách sau khi xóa E:")
# llist.display()

# # Tính độ dài bằng phương pháp đệ quy
# length_recursive = llist.get_length_recursive(llist.head)
# print(f"\nĐộ dài (đệ quy) sau khi xóa E: {length_recursive}")

# # Hoán đổi hai node
# llist.swap_nodes("A", "D")

# # Hiển thị danh sách sau khi hoán đổi
# print("\nDanh sách sau khi hoán đổi A và D:")
# llist.display()

# llist.display()
# llist.reverse_iterative()

# # Sử dụng danh sách liên kết
# llist1 = SinglyLinkedList()
# llist2 = SinglyLinkedList()

# # Thêm các phần tử vào danh sách liên kết 1 (đã sắp xếp)
# llist1.append(1)
# llist1.append(3)
# llist1.append(5)

# # Thêm các phần tử vào danh sách liên kết 2 (đã sắp xếp)
# llist2.append(2)
# llist2.append(4)
# llist2.append(6)

# print("Danh sách liên kết 1:")
# llist1.display()

# print("Danh sách liên kết 2:")
# llist2.display()

# # Gộp hai danh sách liên kết đã sắp xếp
# llist1.merge_sorted_lists(llist2)

# print("\nDanh sách liên kết sau khi gộp:")
# llist1.display()
# Sử dụng danh sách liên kết
# llist = SinglyLinkedList()

# # Thêm các phần tử vào danh sách
# llist.append(1)
# llist.append(2)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(4)
# llist.append(5)

# print("Danh sách ban đầu:")
# llist.display()

# # Xóa các phần tử trùng lặp
# llist.remove_duplicates()

# print("Danh sách sau khi xóa các phần tử trùng lặp:")
# llist.display()

# # Sử dụng danh sách liên kết
# llist = SinglyLinkedList()

# # Thêm các phần tử vào danh sách
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)

# print("Danh sách liên kết:")
# llist.display()

# # Tìm node thứ N từ cuối
# N = 4
# result_node = llist.nth_to_last_node(N)
# if result_node:
#     print(f"Node thứ {N} từ cuối danh sách có giá trị: {result_node.data}")
# else:
#     print(f"Node thứ {N} từ cuối không tồn tại.")
# Sử dụng danh sách liên kết
llist = SinglyLinkedList()

# Thêm các phần tử vào danh sách
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(1)

print("Danh sách liên kết:")
llist.display()

# Kiểm tra xem danh sách có phải là palindrome không
if llist.is_palindrome():
    print("Danh sách là palindrome")
else:
    print("Danh sách không phải là palindrome")
