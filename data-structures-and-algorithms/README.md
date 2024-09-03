- [Data Structures và Algorithms trong Python](#data-structures-và-algorithms-trong-python)
- [Built-in Data Structures](#built-in-data-structures)
  - [List](#list)
    - [Tạo một list](#tạo-một-list)
      - [Bạn có thể tạo một list đơn giản như sau:](#bạn-có-thể-tạo-một-list-đơn-giản-như-sau)
      - [Sử dụng hàm `range()` để tạo một list:](#sử-dụng-hàm-range-để-tạo-một-list)
    - [Truy cập các phần tử trong List:](#truy-cập-các-phần-tử-trong-list)
    - [Thêm, xóa và thay đổi phần tử trong List:](#thêm-xóa-và-thay-đổi-phần-tử-trong-list)
      - [Thêm phần tử](#thêm-phần-tử)
      - [Xóa phần tử](#xóa-phần-tử)
      - [Thay đổi phần tử](#thay-đổi-phần-tử)
      - [Một số phương thức hữu ích khác cho List:](#một-số-phương-thức-hữu-ích-khác-cho-list)
    - [List sclicing](#list-sclicing)
    - [List Comprehension](#list-comprehension)
    - [Tạo một list mới từ một list hiện có](#tạo-một-list-mới-từ-một-list-hiện-có)
    - [Sử dụng if-else trong List Comprehension](#sử-dụng-if-else-trong-list-comprehension)
    - [List comprehension dùng với nhiều list](#list-comprehension-dùng-với-nhiều-list)
  - [Tuple](#tuple)
    - [Tạo một tuple](#tạo-một-tuple)
    - [Truy cập các phần tử trong Tuple](#truy-cập-các-phần-tử-trong-tuple)
    - [Merging tuples](#merging-tuples)
    - [Nested Tuples](#nested-tuples)
    - [Một số thao tác với Tuple](#một-số-thao-tác-với-tuple)
      - [Tìm kiếm](#tìm-kiếm)
      - [Slicing tuple](#slicing-tuple)
    - [Vậy tại sao cần tuple khi đã có list?](#vậy-tại-sao-cần-tuple-khi-đã-có-list)
      - [Ví dụ về sử dụng tuple làm key trong dictionary:](#ví-dụ-về-sử-dụng-tuple-làm-key-trong-dictionary)
  - [Dictionary](#dictionary)
    - [Tạo một dictionary](#tạo-một-dictionary)
      - [Python version 3](#python-version-3)
      - [Python version 3.9.6](#python-version-396)
    - [`dict()` Constructor](#dict-constructor)
      - [Refactor các ví dụ ở trên:](#refactor-các-ví-dụ-ở-trên)
    - [Truy cập giá trị trong Dictionary](#truy-cập-giá-trị-trong-dictionary)
      - [Lợi ích của việc sử dụng `get()`:](#lợi-ích-của-việc-sử-dụng-get)
    - [Dictionary Operations](#dictionary-operations)
      - [Thêm/Cập nhật](#thêmcập-nhật)
      - [Xóa](#xóa)
      - [Độ dài của một Dictionary](#độ-dài-của-một-dictionary)
      - [Kiểm tra Sự Tồn tại của Key](#kiểm-tra-sự-tồn-tại-của-key)
      - [Sao chép nội dung](#sao-chép-nội-dung)
      - [Dictionary Comprehension](#dictionary-comprehension)
  - [Set](#set)
    - [Tạo một set](#tạo-một-set)
    - [Các thao tác cơ bản với Set](#các-thao-tác-cơ-bản-với-set)
      - [Thêm phần tử vào Set](#thêm-phần-tử-vào-set)
      - [Xóa phần tử khỏi Set](#xóa-phần-tử-khỏi-set)
      - [Kiểm tra sự tồn tại của phần tử trong Set](#kiểm-tra-sự-tồn-tại-của-phần-tử-trong-set)
    - [Các phép toán trên tập hợp](#các-phép-toán-trên-tập-hợp)
      - [Union](#union)
      - [Intersection](#intersection)
      - [Difference](#difference)
      - [Symmetric Difference](#symmetric-difference)
    - [Ứng dụng của Set](#ứng-dụng-của-set)
      - [Loại bỏ các phần tử trùng lặp](#loại-bỏ-các-phần-tử-trùng-lặp)
      - [Thực hiện các phép toán tập hợp](#thực-hiện-các-phép-toán-tập-hợp)
    - [Tóm tắt](#tóm-tắt)
      - [List](#list-1)
      - [Tuple](#tuple-1)
      - [Dictionary](#dictionary-1)
      - [Set](#set-1)
- [Stack](#stack)
  - [Các thao tác cơ bản trên stack](#các-thao-tác-cơ-bản-trên-stack)
  - [Determine if Brackets are Balanced](#determine-if-brackets-are-balanced)
    - [Cách tiếp cận](#cách-tiếp-cận)
      - [Giải thích hàm `is_paren_balanced(paren_string)`](#giải-thích-hàm-is_paren_balancedparen_string)
      - [Giải thích hàm `is_match(p1, p2)`](#giải-thích-hàm-is_matchp1-p2)
  - [Reverse String](#reverse-string)
  - [Convert Decimal Integer to Binary](#convert-decimal-integer-to-binary)

# Data Structures và Algorithms trong Python

Cấu trúc dữ liệu và giải thuật là một trong những khái niệm cơ bản nhất của khoa học máy tính. Bài viết này bao gồm một số cấu trúc dữ liệu và thuật toán phổ biến nhất trong Python:

- Built-in Data Structures

- Stack

- Singly Linked Lists

- Circular Linked Lists

- Doubly Linked Lists

- Arrays

- Binary Trees

- Binary Search Trees

- Binary Search

- Recursion

- String Processing

# Built-in Data Structures

Vì chúng ta thường xuyên phải xử lý việc thao tác dữ liệu, nên việc tổ chức dữ liệu một cách hiệu quả và có ý nghĩa là điều vô cùng quan trọng.

Python được trang bị nhiều built-in data structures (cấu trúc dữ liệu tích hợp sẵn) để giúp chúng ta xử lý hiệu quả lượng lớn dữ liệu.

Bốn cấu trúc dữ liệu tích hợp chính mà `Python` cung cấp là:

- List
- Tuple
- Dictionary
- Set

## List

List là một trong những cấu trúc dữ liệu phổ biến và linh hoạt nhất trong Python. Nó cho phép chúng ta lưu trữ các phần tử có kiểu dữ liệu khác nhau trong một vùng chứa. Nội dung của một list được đặt bên trong dấu ngoặc vuông `[]`, và các phần tử được phân tách bởi dấu phẩy `,`.

**Đặc điểm của List**:

- Ordered: Các phần tử được lưu trữ tuyến tính tại một index cụ thể, chúng có một thứ tự nhất định. Khi bạn thêm các phần tử vào list, chúng sẽ được lưu trữ theo thứ tự mà bạn đã thêm vào.
- Có thể thay đổi (Mutable): Bạn có thể thay đổi, thêm, hoặc xóa các phần tử trong list sau khi nó đã được tạo ra.
- Cho phép các giá trị trùng lặp: List có thể chứa các phần tử giống nhau.

### Tạo một list

#### Bạn có thể tạo một list đơn giản như sau:

```python
# Tạo một list với các kiểu dữ liệu khác nhau
mixed_list = [1, "Hello", 3.14, True]
```

#### Sử dụng hàm `range()` để tạo một list:

Hàm range() trong Python được sử dụng để tạo ra một dãy số theo một quy tắc nhất định, `range(start, stop, step)`.

```python
# Tạo list từ 0 đến 9
numbers = list(range(10))
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tạo list từ 5 đến 9
numbers = list(range(5, 10))
print(numbers)  # Output: [5, 6, 7, 8, 9]

# Tạo list từ 0 đến 9 với bước nhảy là 2
numbers = list(range(0, 10, 2))
print(numbers)  # Output: [0, 2, 4, 6, 8]

# Tạo list từ 10 đến 1 với bước nhảy là -1
numbers = list(range(10, 0, -1))
print(numbers)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Truy cập các phần tử trong List:

```python
fruits = ["apple", "banana", "watermelon", "cherry"]

# Truy cập phần tử đầu tiên
print(fruits[0])  # Output: apple

# Truy cập phần tử thứ hai
print(fruits[1])  # Output: banana

# Truy cập phần tử cuối cùng
print(fruits[-1])  # Output: cherry
```

### Thêm, xóa và thay đổi phần tử trong List:

#### Thêm phần tử

Bạn có thể thêm phần tử vào cuối list bằng phương thức `append()` hoặc thêm phần tử vào vị trí cụ thể bằng `insert()`.

```python
fruits = ["apple", "banana", "cherry"]

# Thêm phần tử vào cuối list
fruits.append("orange")

# Thêm phần tử vào vị trí thứ hai
fruits.insert(1, "mango")

print(fruits)  # Output: ['apple', 'mango', 'banana', 'cherry', 'orange']
```

#### Xóa phần tử

Bạn có thể xóa một phần tử bằng `remove()`, `pop()`, hoặc `del`.

```python
fruits = ["apple", "banana", "cherry"]

# Xóa phần tử cụ thể
fruits.remove("banana") # Output: ['apple', 'cherry']

# Xóa phần tử cuối cùng
last_fruit = fruits.pop() # Output: ['apple']

# Xóa phần tử theo index
del fruits[0]

print(fruits)  # Output: []
```

#### Thay đổi phần tử

Bạn có thể thay đổi giá trị của phần tử bằng cách truy cập trực tiếp vào index của nó.

```python
fruits = ["apple", "banana", "cherry"]

# Thay đổi giá trị của phần tử thứ hai
fruits[1] = "blueberry"

print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

#### Một số phương thức hữu ích khác cho List:

- `sort()`: Sắp xếp các phần tử trong list.
- `reverse()`: Đảo ngược thứ tự các phần tử trong list.
- `len()`: Trả về số lượng các phần tử trong list.
- `index()`: Trả về chỉ số của phần tử đầu tiên khớp với giá trị được chỉ định.

```python
numbers = [3, 1, 4, 1, 5, 9]

# Sắp xếp list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Đảo ngược list
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# Độ dài của list
print(len(numbers))  # Output: 6

# Index của phần tử đầu tiên có giá trị 4
print(numbers.index(4))  # Output: 2
```

### List sclicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lấy các phần tử từ index 2 đến index 5 (không bao gồm index 5)
subset = numbers[2:5]
print(subset)  # Output: [2, 3, 4]

# Lấy các phần tử từ đầu đến index 4 (không bao gồm index 4)
start_slice = numbers[:4]
print(start_slice)  # Output: [0, 1, 2, 3]

# Lấy các phần tử từ index 5 đến hết list
end_slice = numbers[5:]
print(end_slice)  # Output: [5, 6, 7, 8, 9]

# Lấy các phần tử từ index 1 đến index 7 với step (bước nhảy) là 2
step_slice = numbers[1:8:2]
print(step_slice)  # Output: [1, 3, 5, 7]

# Đảo ngược list
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Sao chép toàn bộ list
copied_list = numbers[:]
print(copied_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lấy 3 phần tử cuối cùng
last_three = numbers[-3:]
print(last_three)  # Output: [7, 8, 9]

```

### List Comprehension

List Comprehension là một cách ngắn và gọn gàng để tạo ra các list mới từ các list hiện có bằng cách sử dụng cú pháp đơn giản kết hợp giữa vòng lặp `for` và điều kiện `if`

Cú pháp của list comprehension như sau:

```python
new_list = [expression for item in iterable if condition]
```

- expression: Biểu thức được áp dụng lên từng phần tử.
- item: Từng phần tử trong iterable (list, tuple, string, v.v.).
- condition (tuỳ chọn): Điều kiện để chọn các phần tử đưa vào list mới.

### Tạo một list mới từ một list hiện có

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

print(squares)  # Output: [1, 4, 9, 16, 25]
```

### Sử dụng if-else trong List Comprehension

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

print(evens)  # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
results = [x*2 if x % 2 == 0 else x*3 for x in numbers]

print(results)  # Output: [3, 4, 9, 8, 15]
```

### List comprehension dùng với nhiều list

```python
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list) # Output: [(50, 60), (110, 10), (110, 60), (110, 20), (110, 50), (75, 60), (75, 50)]


```

## Tuple

Tuple thì gần giống như list, ngoại trừ việc tuple là immutable (không thể thay đổi). Điều này có nghĩa là sau khi ta tạo một tuple, ta không thể thay đổi, thêm, hoặc xóa các phần tử bên trong nó. Tuy nhiên, nó có thể chứa các phần tử có thể thay đổi (mutable elements) như một list.

Nội dung của tuple được đặt bên trong dấu ngoặc đơn `()` và các phần tử được phân tách bởi dấu phẩy `,`.

### Tạo một tuple

```python
# Tạo một tuple rỗng
empty_tuple = ()

# Tạo một tuple với nhiều phần tử
my_tuple = (1, 2, 3, "Hello", True)

```

Python cũng cho phép ta tạo tuple mà không cần dấu ngoặc đơn, chỉ cần sử dụng dấu phẩy:

```python
my_tuple = 1, 2, 3, "Hello", True
```

### Truy cập các phần tử trong Tuple

```python
my_tuple = (1, 2, 3, "Hello", True)

# Truy cập phần tử đầu tiên
print(my_tuple[0])  # Output: 1

# Truy cập phần tử cuối cùng
print(my_tuple[-1])  # Output: True
```

### Merging tuples

Tuples có thể được merged bằng cách sử dụng toán tử `+`.

```python
hero1 = ("Batman", "Wonder Woman")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team) # Output: ('Batman', 'Wonder Woman', 'Wonder Woman', 'Diana Prince')

```

### Nested Tuples

```python
nested_tuple = (1, 2, (3, 4), 5)

# Truy cập phần tử bên trong tuple lồng nhau
print(nested_tuple[2][1])  # Output: 4
```

Một ví dụ khác về nested tuples:

```python
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team) # Output: (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))

```

### Một số thao tác với Tuple

#### Tìm kiếm

Chúng ta có thể kiểm tra xem một phần tử có tồn tại trong một tuple hay không bằng cách sử dụng toán tử `in` như sau:

```python
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities) # Output: False
```

Hàm `index()` có thể cung cấp cho chúng ta index của một giá trị cụ thể:

```python
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo")) # Output: 3
```

#### Slicing tuple

Tương tự như với list

```python
my_tuple = (1, 2, 3, 4, 5)
slice_tuple = my_tuple[1:4]
print(slice_tuple)  # Output: (2, 3, 4)

```

### Vậy tại sao cần tuple khi đã có list?

- Immutable: Tính không thể thay đổi giúp tuple an toàn hơn khi ta cần lưu trữ các giá trị không muốn bị thay đổi sau khi tạo ra.
- Hiệu suất: Tuple thường có hiệu suất tốt hơn list trong các tình huống không cần thay đổi dữ liệu.
- Tuple có thể làm key cho dictionary: Do tính immutable, tuple có thể được sử dụng làm key trong dictionary (trong khi list thì không).

#### Ví dụ về sử dụng tuple làm key trong dictionary:

```python
# Tạo dictionary với khóa là tuple (tọa độ) và giá trị là tên thành phố
cities = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "London",
    (48.8566, 2.3522): "Paris"
}

# Truy cập tên thành phố dựa trên tọa độ
location = (40.7128, -74.0060)
city_name = cities[location]
print(f"Thành phố tại tọa độ {location} là {city_name}")
# Output: Thành phố tại tọa độ (40.7128, -74.0060) là New York
```

[Tham khảo thêm](https://stackoverflow.com/questions/1938614/in-what-case-would-i-use-a-tuple-as-a-dictionary-key)

## Dictionary

So với list hoặc tuple, dictionary có cấu trúc phức tạp hơn một chút.

Dictionary trong Python là một cấu trúc dữ liệu cho phép ta lưu trữ các cặp key-value (khóa-giá trị). Mỗi khóa là duy nhất và được sử dụng để truy xuất giá trị tương ứng. Dictionary là một kiểu dữ liệu mutable, có nghĩa là ta có thể thay đổi nội dung của nó sau khi tạo.

Trong Python, nội dung của dictionary được đặt bên trong dấu ngoặc nhọn `{}`, và mỗi cặp key-value được phân tách bởi dấu hai chấm `:`. Các cặp key-value được phân tách bởi dấu phẩy `,`.

Trong các phiên bản Python trước 3.6, dictionary là unordered. Kể từ Python 3.7, các dictionary trở nên ordered theo mặc định. Ta sẽ xem ví dụ ngay dưới đây

### Tạo một dictionary

```python
empty_dict = {}  # Dictionary rỗng
print(empty_dict) # {}
```

#### Python version 3

```python
films = {"The Gentlemen": 2019,
            "The Terminal List": 2022,
            "Guy Ritchie's The Covenant": 2023}
print(films) # {'The Terminal List': 2022, "Guy Ritchie's The Covenant": 2023, 'The Gentlemen': 2019}

```

#### Python version 3.9.6

```python
films = {"The Gentlemen": 2019,
            "The Terminal List": 2022,
            "Guy Ritchie's The Covenant": 2023}
print(films) # {'The Gentlemen': 2019, 'The Terminal List': 2022, "Guy Ritchie's The Covenant": 2023}
```

### `dict()` Constructor

Như tên gọi, `dict()` constructor có thể được sử dụng để tạo ra một dictionary.

Nếu các khóa (keys) của chúng ta là các chuỗi đơn giản không có ký tự đặc biệt, chúng ta có thể tạo các item trong dictionary trực tiếp trong constructor. Trong trường hợp này, giá trị sẽ được gán cho các khóa bằng cách sử dụng toán tử `=`.

Việc sử dụng `dict()` có thể làm cho code của ta ngắn gọn và dễ đọc hơn trong một số trường hợp nhất định.

#### Refactor các ví dụ ở trên:

Thay vì viết:

```python
empty_dict = {}
```

Có thể viết lại như sau:

```python
empty_dict = dict()
```

Thay vì viết:

```python
phone_book = {
    'John': 123456789,
    'Alice': 987654321,
    'Bob': 456789123
}
```

Ta có thể viết lại thành:

```python
phone_book = dict(John=123456789, Alice=987654321, Bob=456789123)
```

### Truy cập giá trị trong Dictionary

Đối với nhiều người, đây là điểm mà dictionary có ưu thế hơn so với list hoặc tuple. Vì không có các chỉ mục tuyến tính (linear indices), chúng ta không cần phải theo dõi vị trí lưu trữ của các giá trị.

Thay vào đó, chúng ta có thể truy cập một giá trị của dict theo cú pháp `[key]`. Điều này có ý nghĩa hơn so với việc sử dụng các chỉ số nguyên (integer indices) mà chúng ta sử dụng cho tuples và lists.

Ngoài ra, chúng ta cũng có thể sử dụng phương thức `get()` để truy cập giá trị như sau:

```python
# Ví dụ về việc truy cập giá trị bằng key trong dictionary
phone_book = {'John': 123456789, 'Alice': 987654321, 'Bob': 456789123}

# Truy cập giá trị bằng dấu ngoặc vuông []
john_number = phone_book['John']
print(john_number)  # Output: 123456789

# Truy cập giá trị bằng phương thức get()
alice_number = phone_book.get('Alice')
print(alice_number)  # Output: 987654321
```

#### Lợi ích của việc sử dụng `get()`:

An toàn hơn khi key không tồn tại: Khi sử dụng dấu ngoặc vuông `[]` để truy cập một giá trị mà key không tồn tại trong dictionary, Python sẽ phát sinh lỗi `KeyError`. Tuy nhiên, với phương thức `get()`, nếu key không tồn tại, thay vì phát sinh lỗi, Python sẽ trả về `None` hoặc một giá trị mặc định mà ta có thể xác định.

Ví dụ

```python
# Sử dụng dấu ngoặc vuông có thể gây lỗi nếu key không tồn tại
try:
  non_existent = phone_book['Michael']  # KeyError nếu 'Michael' không có trong dictionary
except KeyError:
  print("Key không tồn tại")

# Sử dụng get() để tránh lỗi
non_existent = phone_book.get('Michael')
print(non_existent)  # Output: None (không gây lỗi)

# Trả về giá trị mặc định khi key không tồn tại
non_existent_with_default = phone_book.get('Michael', 'Không tìm thấy')
print(non_existent_with_default)  # Output: Không tìm thấy
```

### Dictionary Operations

#### Thêm/Cập nhật

```python
# Tạo một dictionary
phone_book = {'John': 123456789, 'Alice': 987654321}

# Thêm item mới
phone_book['Bob'] = 456789123
print(phone_book)  # Output: {'John': 123456789, 'Alice': 987654321, 'Bob': 456789123}

# Cập nhật item hiện có
phone_book['Alice'] = 111111111
print(phone_book)  # Output: {'John': 123456789, 'Alice': 111111111, 'Bob': 456789123}
```

#### Xóa

- Dùng `del`: Xóa một mục bằng cách chỉ định key.
- Dùng `pop()`: Xóa một mục và trả về giá trị của mục đó.
- Dùng `popitem()`: Xóa và trả về cặp `key-value` cuối cùng trong dictionary.
- Dùng `clear()`: Xóa tất cả các mục trong dictionary.

```python
# Xóa item bằng del
del phone_book['John']
print(phone_book)  # Output: {'Alice': 111111111, 'Bob': 456789123}

# Xóa item bằng pop()
bob_number = phone_book.pop('Bob')
print(bob_number)  # Output: 456789123
print(phone_book)  # Output: {'Alice': 111111111}

# Xóa và trả về item cuối cùng bằng popitem()
last_item = phone_book.popitem()
print(last_item)  # Output: ('Alice', 111111111)
print(phone_book)  # Output: {}

# Xóa tất cả các item bằng clear()
phone_book.clear()
print(phone_book)  # Output: {}

```

#### Độ dài của một Dictionary

```python
phone_book = {'John': 123456789, 'Alice': 111111111, 'Bob': 456789123}
length = len(phone_book)
print(length)  # Output: 3
```

#### Kiểm tra Sự Tồn tại của Key

Ta có thể kiểm tra xem một key có tồn tại trong dictionary hay không bằng cách sử dụng từ khóa `in`:

```python
if 'Alice' in phone_book:
    print("Alice có trong danh bạ")
else:
    print("Alice không có trong danh bạ")

# Output: Alice có trong danh bạ
```

#### Sao chép nội dung

```python
# Sao chép bằng copy()
phone_book_copy = phone_book.copy()
print(phone_book_copy) # Output: {'John': 123456789, 'Alice': 111111111, 'Bob': 456789123}

# Sao chép bằng dict()
phone_book_copy_2 = dict(phone_book)
print(phone_book_copy_2) # Output: {'John': 123456789, 'Alice': 111111111, 'Bob': 456789123}

```

#### Dictionary Comprehension

Dictionary Comprehension là một cách ngắn gọn và mạnh mẽ để tạo dictionary mới từ một iterable (như list, tuple, hay một dictionary khác). Cú pháp của nó tương tự như List Comprehension nhưng kết quả là một dictionary.

```python
# Tạo dictionary với các số và bình phương của chúng
squares = {x: x**2 for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary Comprehension từ một dictionary có sẵn
phone_book = {'John': 123456789, 'Alice': 111111111, 'Bob': 456789123}
filtered_phone_book = {k: v for k, v in phone_book.items() if v != 111111111}
print(filtered_phone_book)  # Output: {'John': 123456789, 'Bob': 456789123}
```

## Set

Set trong Python là một cấu trúc dữ liệu được sử dụng để lưu trữ một tập hợp các phần tử mà mỗi phần tử là duy nhất và không có thứ tự (unordered).

Ta có thể tạo một set bằng cách đặt các phần tử vào trong dấu ngoặc nhọn `{}`, hoặc sử dụng hàm `set()`.

### Tạo một set

```python
# Tạo một set rỗng
empty_set = set()
print(empty_set)  # Output: set()

# Tạo một set
random_set = {"Educative", 1408, 3.142, (True, False)}
print(random_set) # Output: {1408, (True, False), 3.142, 'Educative'}

# Tạo một set từ một chuỗi, các ký tự sẽ là các phần tử trong set
char_set = set("hello")
print(char_set)  # Output: {'h', 'e', 'l', 'o'}
```

### Các thao tác cơ bản với Set

#### Thêm phần tử vào Set

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

#### Xóa phần tử khỏi Set

Ta có thể xóa một phần tử khỏi set bằng cách sử dụng `remove()` hoặc `discard()`:

- `remove()` sẽ phát sinh lỗi nếu phần tử không tồn tại trong set.
- `discard()` sẽ không phát sinh lỗi nếu phần tử không tồn tại.

```python
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

my_set.discard(5)  # Không phát sinh lỗi mặc dù 5 không có trong set
print(my_set)  # Output: {1, 3, 4}
```

#### Kiểm tra sự tồn tại của phần tử trong Set

Ta có thể sử dụng toán tử `in` để kiểm tra xem một phần tử có tồn tại trong set hay không.

```python
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False
```

### Các phép toán trên tập hợp

#### Union

Tạo một set mới chứa tất cả các phần tử từ cả hai set.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

#### Intersection

Tạo một set mới chứa các phần tử có trong cả hai set.

```python
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
```

#### Difference

Tạo một set mới chứa các phần tử có trong set đầu tiên nhưng không có trong set thứ hai.

```python
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

#### Symmetric Difference

Tạo một set mới chứa các phần tử có trong set này hoặc set kia nhưng không có trong cả hai set.

```python
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

### Ứng dụng của Set

#### Loại bỏ các phần tử trùng lặp

Set rất hữu ích khi ta cần loại bỏ các phần tử trùng lặp từ một danh sách.

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}
```

#### Thực hiện các phép toán tập hợp

Như đã đề cập, set cho phép ta dễ dàng thực hiện các phép toán tập hợp như hợp, giao, hiệu, hiệu đối xứng.

### Tóm tắt

#### List

Đặc điểm: List là một cấu trúc dữ liệu có thứ tự (ordered), có thể thay đổi (mutable), và cho phép các phần tử trùng lặp.

#### Tuple

Đặc điểm: Tuple là một cấu trúc dữ liệu có thứ tự (ordered) nhưng không thể thay đổi (immutable), và cũng cho phép các phần tử trùng lặp.

#### Dictionary

Đặc điểm: Dictionary là một cấu trúc dữ liệu không có thứ tự (unordered) trong các phiên bản Python trước 3.7, và có thứ tự (ordered) từ Python 3.7 trở đi. Dictionary có thể thay đổi (mutable) và lưu trữ các cặp key-value (khóa-giá trị), trong đó các key là duy nhất.

#### Set

Đặc điểm: Set là một cấu trúc dữ liệu không có thứ tự (unordered) và không chứa các phần tử trùng lặp. Set có thể thay đổi (mutable).

# Stack

Stack là một cấu trúc dữ liệu tuân theo nguyên tắc LIFO (Last In, First Out), nghĩa là phần tử được thêm vào cuối cùng sẽ được lấy ra đầu tiên.

Giả sử ta có 4 cuốn sách và sắp xếp nó thành một stack:

![](images/stack.png)

Ví dụ, nếu anh muốn lấy Book A và nó đang nằm ở dưới đáy của chồng sách, anh sẽ phải lần lượt lấy Book D, rồi Book C, và Book B xuống trước, rồi mới có thể lấy được Book A.

Stack trong lập trình hoạt động rất giống với chồng sách mà ta thấy ở trên. Stack là một cấu trúc dữ liệu cho phép ta "đặt" (push) bất kỳ đối tượng, biến hoặc giá trị nào lên trên cùng, giống như cách ta đặt sách lên chồng. Khi ta muốn "lấy" (pop) một giá trị, ta sẽ lấy giá trị ở trên cùng trước, tương tự như lấy cuốn sách trên cùng của chồng sách.

## Các thao tác cơ bản trên stack

- Push: Thêm một phần tử vào đỉnh (top) của stack.
- Pop: Xóa và trả về phần tử ở đỉnh của stack.
- Peek: Trả về phần tử ở đỉnh của stack mà không xóa nó.
- isEmpty: Kiểm tra xem stack có rỗng hay không.
- isFull: Kiểm tra xem stack có đầy không (nếu stack có giới hạn kích thước).

Giờ chúng ta sẽ tạo class Stack:

```python
"""
Stack Data Structure.
"""
class Stack:
    def __init__(self):
        # Khởi tạo stack như một danh sách trống
        self.stack = []

    def push(self, item):
        # Thêm một phần tử vào đỉnh của stack
        self.stack.append(item)

    def pop(self):
        # Xóa và trả về phần tử ở đỉnh của stack
        # Kiểm tra xem stack có rỗng không để tránh lỗi
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty, cannot pop."

    def peek(self):
        # Trả về phần tử ở đỉnh của stack mà không xóa nó
        # Kiểm tra xem stack có rỗng không để tránh lỗi
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty, no top element to peek."

    def is_empty(self):
        # Kiểm tra xem stack có rỗng không
        return len(self.stack) == 0

    def size(self):
        # Trả về số lượng phần tử trong stack
        return len(self.stack)

    def __str__(self):
        # Trả về nội dung của stack dưới dạng chuỗi để dễ quan sát
        return str(self.stack)

# Sử dụng lớp Stack
stack = Stack()

# Thêm các phần tử vào stack
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack sau khi push các phần tử:", stack) # Output: Stack sau khi push các phần tử: [10, 20, 30]

# Xem phần tử ở đỉnh của stack
print("Phần tử ở đỉnh của stack (peek):", stack.peek()) # Output: Phần tử ở đỉnh của stack (peek): 30

# Xóa phần tử ở đỉnh của stack
print("Phần tử được lấy ra từ stack (pop):", stack.pop()) # Output: Phần tử được lấy ra từ stack (pop): 30
print("Stack sau khi pop:", stack) # Output: Stack sau khi pop: [10, 20]

# Kiểm tra xem stack có rỗng không
print("Stack có rỗng không?", stack.is_empty()) # Output: Stack có rỗng không? False

# Trả về kích thước của stack
print("Kích thước của stack:", stack.size()) # Output: Kích thước của stack: 2

```

## Determine if Brackets are Balanced

Cho một chuỗi chứa các dấu ngoặc `(), {}, []`. Nhiệm vụ của chúng ta là viết một hàm để kiểm tra xem các dấu ngoặc này có được sắp xếp hợp lệ hay không.

Ví dụ về Balanced Brackets

- `{ }`
- `{ } { }`
- `( ( { [ ] } ) )`

Ví dụ về Unbalanced Brackets

- `( ( )`
- `{ { { ) } ]`
- `[ ] [ ] ] ]`

### Cách tiếp cận

- Sử dụng một stack để lưu trữ các dấu mở ngoặc.
- Duyệt qua từng ký tự trong chuỗi:
  - Nếu gặp dấu mở ngoặc (`(, {, [`), thì đẩy nó vào stack.
  - Nếu gặp dấu đóng ngoặc (`), }, ]`):
    - Kiểm tra xem stack có rỗng không (nếu rỗng nghĩa là chuỗi không cân bằng).
    - Lấy phần tử trên cùng của stack ra và kiểm tra xem nó có tương ứng với dấu đóng hiện tại không. Nếu không, chuỗi không cân bằng.
- Cuối cùng, nếu stack rỗng thì chuỗi cân bằng, nếu không rỗng thì chuỗi không cân bằng.

`stack.py`

```python
"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
```

`main.py`

```python
from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))")) # Output: True


print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]")) # Output: False

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]")) # Output: True

```

#### Giải thích hàm `is_paren_balanced(paren_string)`

Chúng ta khai báo một `Stack s` (ban đầu là rỗng), và hai biến `is_balanced` và `index` được gán giá trị lần lượt là `True` và `0`.

`is_balanced` sẽ được sử dụng để theo dõi trạng thái cân bằng của các dấu ngoặc, và `index` sẽ dùng để duyệt qua các ký tự trong chuỗi `paren_string`.

Vòng lặp `while` chạy cho đến khi chúng ta đã duyệt qua toàn bộ chuỗi hoặc cho đến khi phát hiện rằng chuỗi không cân bằng (`is_balanced` trở thành `False`).

Vòng lặp này duyệt qua từng ký tự trong chuỗi `paren_string` bằng cách sử dụng biến `index`. Ký tự hiện tại sẽ được lưu trong biến `paren`.

Tiếp theo, chương trình kiểm tra xem ký tự hiện tại (`paren`) có phải là một trong các dấu ngoặc mở (`(, {, [`) không.
Nếu đúng, dấu ngoặc mở được đẩy vào stack `s` bằng thao tác `s.push(paren)`.

Nếu ký tự không phải là dấu ngoặc mở:

- Kiểm tra xem stack `s` có rỗng không. Nếu stack rỗng, điều này có nghĩa là có một dấu ngoặc đóng mà không có dấu ngoặc mở tương ứng, do đó chuỗi không cân bằng (`is_balanced = False`), và chúng ta thoát khỏi vòng lặp (`break`).
- Nếu stack không rỗng:
  - Chúng ta lấy phần tử trên cùng của stack (`top = s.pop()`) và kiểm tra xem nó có khớp với dấu ngoặc đóng hiện tại hay không bằng cách sử dụng hàm `is_match`.
  - Nếu dấu ngoặc mở ở đỉnh của stack không khớp với dấu ngoặc đóng hiện tại, chuỗi không cân bằng (`is_balanced = False`), và chúng ta thoát khỏi vòng lặp (`break`).

Tiếp theo, tăng giá trị `index` để tiếp tục duyệt qua ký tự tiếp theo trong chuỗi.

Sau khi vòng lặp `while` kết thúc, chúng ta kiểm tra xem stack có rỗng và biến `is_balanced` có vẫn là `True` không.

- Nếu cả hai điều kiện đều đúng, điều đó có nghĩa là chuỗi có các dấu ngoặc cân bằng hoàn toàn, và hàm sẽ trả về `True`.

Nếu stack không rỗng hoặc biến `is_balanced` là `False`, điều này có nghĩa là chuỗi không cân bằng, và hàm sẽ trả về `False`.

#### Giải thích hàm `is_match(p1, p2)`

Hàm `is_match` được sử dụng để kiểm tra xem hai ký tự, cụ thể là `p1` và `p2`, có phải là một cặp dấu ngoặc hợp lệ hay không. Để `p1` và `p2` khớp nhau:

- `p1` phải là một dấu ngoặc mở (`(, {, [`).
- `p2` phải là dấu ngoặc đóng tương ứng (`), }, ]`).

Nếu `p1` và `p2` khớp nhau theo đúng điều kiện trên, hàm sẽ trả về `True`. Nếu không, hàm sẽ trả về `False`.

## Reverse String

Thuật toán để đảo ngược một chuỗi bằng cách sử dụng stack là khá đơn giản và hiệu quả. Thuật toán này hoạt động dựa trên tính chất LIFO (Last-In, First-Out) của stack, nghĩa là phần tử được đưa vào sau cùng sẽ được lấy ra đầu tiên. Khi chúng ta đẩy tất cả các ký tự của chuỗi vào stack, và sau đó lấy chúng ra theo thứ tự ngược lại, chúng ta sẽ thu được một chuỗi đã được đảo ngược.

- Bằng cách duyệt qua từng ký tự trong chuỗi và đẩy nó vào stack, chúng ta lưu trữ các ký tự theo thứ tự ngược lại trong stack.
- Khi chúng ta lần lượt lấy từng ký tự ra từ stack, ký tự đầu tiên được đẩy vào sẽ là ký tự cuối cùng được lấy ra, giúp tạo ra chuỗi đảo ngược.

`main.py`

```python
from stack import Stack
def reverse_string(stack, input_str):

    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
input_str = "!olbiV ot emocleW"
print(reverse_string(stack, input_str)) # Output: Welcome to Viblo!
```

- Vòng lặp for này lặp qua từng ký tự trong chuỗi `input_str` bằng cách sử dụng index `i`.
- Mỗi ký tự từ `input_str[i]` được đưa vào stack thông qua phương thức `stack.push(input_str[i])`.
- Kết quả là tất cả các ký tự của `input_str` được đẩy vào stack theo thứ tự từ đầu đến cuối.
- Biến `rev_str` được khởi tạo là một chuỗi trống `("")`.
- Biến này sẽ được sử dụng để xây dựng chuỗi đã được đảo ngược.
- Vòng lặp while này tiếp tục chạy miễn là stack không rỗng (`not stack.is_empty()`).
- Trong mỗi lần lặp, phần tử trên cùng của stack được lấy ra bằng phương thức `stack.pop()` và được nối thêm vào chuỗi `rev_str`.
- Vì stack là cấu trúc dữ liệu LIFO (Last-In, First-Out), các ký tự được đưa vào sau cùng sẽ được lấy ra trước, do đó `rev_str` sẽ chứa các ký tự theo thứ tự ngược lại so với chuỗi ban đầu.
- Sau khi vòng lặp while kết thúc (nghĩa là stack đã rỗng), chuỗi `rev_str` sẽ chứa phiên bản đảo ngược của `input_str`.
- Hàm `reverse_string` trả về chuỗi `rev_str` này.

## Convert Decimal Integer to Binary

`main.py`

```python
from stack import Stack

def convert_int_to_bin(dec_num):

    if dec_num == 0:
        return 0

    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convert_int_to_bin(56)) # Output: 111000
print(convert_int_to_bin(2)) # Output: 10
print(convert_int_to_bin(32)) # Output: 100000
print(convert_int_to_bin(10)) # Output: 1010
print(int(convert_int_to_bin(56),2)==56) # Output: True
```

Hàm này chuyển đổi một số nguyên thập phân (`dec_num`) sang dạng nhị phân bằng cách chia liên tục số đó cho `2` và lưu trữ phần dư vào stack. Sau khi quá trình chia hoàn tất, các phần dư sẽ được lấy ra từ stack để tạo thành số nhị phân.

- Hàm bắt đầu bằng việc kiểm tra nếu `dec_num` bằng `0`, hàm sẽ trả về `0`.
- Một đối tượng stack `s` được khởi tạo. Stack này sẽ được sử dụng để lưu trữ các phần dư khi thực hiện phép chia.

- Vòng lặp while chạy cho đến khi `dec_num` lớn hơn `0`. Ở mỗi vòng lặp:
  - `remainder = dec_num % 2`: Tính phần dư của `dec_num` khi chia cho `2`. Phần dư này sẽ là một trong các chữ số trong biểu diễn nhị phân.
  - `s.push(remainder)`: Phần dư được đẩy vào stack.
  - `dec_num = dec_num // 2`: Cập nhật giá trị `dec_num` bằng thương của phép chia `dec_num` cho `2`.
- Phần dư của mỗi phép chia biểu diễn các bit nhị phân từ phải sang trái, vì vậy các bit này được đẩy vào stack để sau này có thể lấy ra theo thứ tự ngược lại.

- Sau khi đã đẩy tất cả các phần dư vào stack, hàm tạo một chuỗi trống `bin_num` để lưu trữ số nhị phân.
- Vòng lặp while tiếp tục chạy cho đến khi stack rỗng (`s.is_empty()` trả về `True`):

  - `bin_num += str(s.pop())`: Mỗi lần lặp, phần tử trên cùng của stack (là một chữ số nhị phân) được lấy ra và nối vào chuỗi `bin_num`.
  - Vì các phần tử được đẩy vào stack từ phải sang trái, nên khi lấy ra từ stack, chúng sẽ được xếp đúng thứ tự để tạo thành số nhị phân.

- Cuối cùng, hàm trả về chuỗi nhị phân `bin_num`, là kết quả của quá trình chuyển đổi từ số nguyên thập phân ban đầu.

**Ví dụ**
Nếu `dec_num = 10`, thì:

- 10 chia 2 dư 0 (push 0 vào stack)
- 5 chia 2 dư 1 (push 1 vào stack)
- 2 chia 2 dư 0 (push 0 vào stack)
- 1 chia 2 dư 1 (push 1 vào stack)

Stack sẽ chứa `[0, 1, 0, 1]`. Sau khi `pop` từ stack và nối lại, chuỗi kết quả sẽ là "`1010`", tức là dạng nhị phân của `10`.

<!-- ## Linked Lists

## Singly Linked List

## Circular Linked Lists

## Doubly Linked List

## Arrays -->
