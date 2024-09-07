- [Các khái niệm cơ bản trong OOP](#các-khái-niệm-cơ-bản-trong-oop)
  - [Khởi tạo object trong Python](#khởi-tạo-object-trong-python)
  - [Class variables và instance variables](#class-variables-và-instance-variables)
- [Methods trong Python](#methods-trong-python)
  - [Instance Method](#instance-method)
    - [`self`](#self)
  - [Class Method trong Python](#class-method-trong-python)
  - [Static methods trong Python](#static-methods-trong-python)
- [Access Modifiers trong Python](#access-modifiers-trong-python)
  - [Public attributes trong Python](#public-attributes-trong-python)
  - [Private attributes trong Python](#private-attributes-trong-python)
  - [Truy cập private attributes trong main code](#truy-cập-private-attributes-trong-main-code)
- [Information Hiding trong Python](#information-hiding-trong-python)
  - [Encapsulation (Tính đóng gói) trong Python](#encapsulation-tính-đóng-gói-trong-python)
- [Inheritance (tính kế thừa) trong Python](#inheritance-tính-kế-thừa-trong-python)
  - [Triển khai inheritance trong Python](#triển-khai-inheritance-trong-python)
  - [`super()` function](#super-function)
- [Polymorphism (Tính đa hình) trong Python](#polymorphism-tính-đa-hình-trong-python)
  - [Dẫn nhập về tính đa hình trong Python](#dẫn-nhập-về-tính-đa-hình-trong-python)
  - [Triển khai tính đa hình (polymorphism) sử dụng tính kế thừa (inheritance) trong Python](#triển-khai-tính-đa-hình-polymorphism-sử-dụng-tính-kế-thừa-inheritance-trong-python)
  - [Method overriding (ghi đè phương thức) trong Python](#method-overriding-ghi-đè-phương-thức-trong-python)
  - [Method overloading (nạp chồng phương thức) trong Python](#method-overloading-nạp-chồng-phương-thức-trong-python)
  - [Operator overloading (nạp chồng toán tử) trong Python](#operator-overloading-nạp-chồng-toán-tử-trong-python)
  - [Triển khai tính đa hình (polymorphism) sử dụng `duck typing` trong Python](#triển-khai-tính-đa-hình-polymorphism-sử-dụng-duck-typing-trong-python)
- [Tính trừu tượng (Abstraction) và Abstract Base Class trong Python](#tính-trừu-tượng-abstraction-và-abstract-base-class-trong-python)
  - [Tại sao phải dùng ABC?](#tại-sao-phải-dùng-abc)
  - [Syntax của Abstract Base Class trong Python](#syntax-của-abstract-base-class-trong-python)

# Các khái niệm cơ bản trong OOP

Dưới đây là những khái niệm cơ bản trong lập trình hướng đối tượng:

- properties
- method
- class
- object
- instance

Trong thực tế, chúng ta có thể thấy rất nhiều objects xung quanh chúng ta như các tòa nhà, con người, v.v... Hay khi đi làm, mỗi người trong công ty đều có mã định danh (ID), mức lương (salary), phòng ban (department), v.v... khác nhau nhưng họ đều là nhân viên (employee).

Vậy để dễ quản lý, chúng ta coi `Employee` là 1 **class** - là tập hợp các employee có đặc điểm chung về **properties** (ID, salary, department) nhưng khác giá trị.

Ví dụ `Employee A`, `Employee B` là hai **objects** thuộc **class** `Employee`.

**Method** có thể được coi là các hành vi (behaviors) của object. Method thể truy cập vào các properties, và các methods khác của class mà nó thuộc về. Methods có thể nhận và trả về giá trị, hoặc chỉ thực hiện các hành động nào đó trên object của class.

Ví dụ object `Employee` sẽ có methods như tính thuế thu nhập dựa trên lương (`tax()`), hay cung cấp thông tin của employee (`employee_info()`).

Một **Instance** là một variable mà giữ địa chỉ bộ nhớ (`memory address`) của object đó. Ví dụ cho dễ hiểu thì:

- Class là một bản thiết kế chi tiết cho ngôi nhà
- Object là tất cả những ngôi nhà được xây dựng dựa trên bản thiết kế đó
- Instance là một căn nhà cụ thể (nhà của A, nhà của B)

## Khởi tạo object trong Python

Trong Python, ta có **initializer**, như tên gọi của nó, là một method được dùng để khởi tạo một object của một class. Method này cũng tương tự các method khác nhưng khác ở chỗ **initializer** thì đã được đặt tên là: `__init__`.

Initializer được gọi tự động khi một object của class được tạo. Đây là một method đặc biệt giúp chúng ta xác định và gán giá trị cho các variables của instance. Tương tự các method khác, initializer cũng có thể có optional parameters (tham số mặc định).

Dưới đây là ví dụ khi objects của `Employee` class được tạo, một với tham số mặc định, một với tham số của chúng ta truyền vào.

```Python
class Employee:
    # Khai báo properties và gán giá trị cho chúng
    def __init__(self, ID = None, salary = 0, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department

# Tạo một object của class Employee với các tham số mặc định
steve = Employee()

# Tạo một object của class Employee với tham số của chúng ta
mark = Employee("3789", 2500, "Human Resources")

# In ra properties của mark và steve
print("Steve")
print("ID :", steve.ID)
print("Salary :", steve.salary)
print("Department :", steve.department)
print("Mark")
print("ID :", mark.ID)
print("Salary :", mark.salary)
print("Department :", mark.department)
```

Output

```terminal
Steve
ID : None
Salary : 0
Department : None
Mark
ID : 3789
Salary : 2500
Department : Human Resources
```

## Class variables và instance variables

Trong Python, properties được chia làm 2 loại:

- Class variables
- Instance variables

### Class variables trong Python

Tất cả các objects của class đều được phép truy cập và thay đổi giá trị của **class variable**. Khi thay đổi giá trị của **class variable** thì giá trị của property này sẽ thay đổi trong tất cả các object của class.

### Instance variables

**Instance variables** là của riêng với mỗi objects. Sự thay đổi ở instance variables của object nào thì chỉ ảnh hưởng đến object đó.

### Khai báo class variable và instance variable

**Class variables** được khai báo ngoài `initializer` và **instance variables** được khai báo trong scope của `initializer`

```python
class Player:
    team_name = 'Manchester City'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
```

Chúng ta phải sử dụng **class variable** đúng cách vì như đã nói, chúng được chia sẻ cho tất cả các objects thuộc class và có thể thay đổi giá trị của **class variable** bằng cách sử dụng bất kỳ objects nào.

Dưới đây là ví dụ về sử dụng class variable **_`sai`_**.

```python
class Player:
    team_name = 'Manchester City'  # class variables
    former_teams = [] # class variables
    def __init__(self, name):
        self.name = name  # instance variables

# Tạo 2 objects thuộc class Player
p1 = Player("David Silva")
p2 = Player("Yaya Toure")

# Dùng built-in method `append` để thêm giá trị vào variable `former_teams`
p1.former_teams.append('Celta Vigo') # dùng sai class variable
p2.former_teams.append('Barcelona') # dùng sai class variable

# In properties của các objects
print("Name:", p1.name)
print("Team Name:", p1.team_name)
print(p1.former_teams)
print("Name:", p2.name)
print("Team Name:", p2.team_name)
print(p2.former_teams)
```

Output

```terminal
Name: David Silva
Team Name: Manchester City
['Celta Vigo', 'Barcelona']
Name: Yaya Toure
Team Name: Manchester City
['Celta Vigo', 'Barcelona']
```

Ở ví dụ trên, trong khi **instance variable** `name` là riêng biệt cho mỗi object thuộc `Player` class. Thì **class variable** `former_teams`, có thể truy cập bởi tất cả các object thuộc class nên nó đã được cập nhật giá trị 2 lần.

Chúng ta đang lưu trữ tất cả các cầu thủ hiện đang chơi cho cùng một đội, nhưng mỗi cầu thủ trong đội phần lớn sẽ không cùng đội bóng cũ. Để tránh vấn đề này, triển khai chính xác cho ví dụ trên sẽ như sau:

```python
class Player:
    team_name = 'Manchester City'  # class variables

    def __init__(self, name):
        self.name = name  # instance variables
        self.former_teams = [] # instance variables

# Tạo 2 objects thuộc class Player
p1 = Player("David Silva")
p2 = Player("Yaya Toure")

# Dùng built-in method `append` để thêm giá trị vào variable `former_teams`
p1.former_teams.append('Celta Vigo') # dùng sai class variable
p2.former_teams.append('Barcelona') # dùng sai class variable

# In properties của các objects
print("Name:", p1.name)
print("Team Name:", p1.team_name)
print(p1.former_teams)
print("Name:", p2.name)
print("Team Name:", p2.team_name)
print(p2.former_teams)
```

Output

```terminal
Name: David Silva
Team Name: Manchester City
['Celta Vigo']
Name: Yaya Toure
Team Name: Manchester City
['Barcelona']
```

Bây giờ, `former_teams` đã là của riêng của mỗi object `Player`, và sẽ được truy cập bởi object đó mà thôi.

### Một ví dụ khác về sử dụng class variables

```python
class Player:
    team_name = 'Manchester City' # class variables
    team_members = [] # class variables

    def __init__(self, name):
        self.name = name # instance variables
        self.former_teams = [] # instance variables

        # sử dụng method append để mỗi lần tạo ra object Player
        # thì sẽ tự thêm `name` của player đó vào class variable team_members
        self.team_members.append(self.name)


p1 = Player('David Silva')
p2 = Player('Yaya Toure')

print("Team Name:", p1.team_name)
print("Team Members:")
print(p1.team_members)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.team_members)
```

Output

```terminal
Team Name: Manchester City
Team Members:
['David Silva', 'Yaya Toure']

Name: Yaya Toure
Team Members:
['David Silva', 'Yaya Toure']
```

Ở ví dụ trên, chúng ta đã khai báo class variable `team_members`, một list được chia sẻ với tất cả các object thuộc `Player` class. Mỗi object `Player` được tạo ra, `name` của object sẽ được thêm vào list `team_members`, chúng ta có thể thấy `p1` và `p2` đều có thể truy cập vào `team_members`.

# Methods trong Python

Trong phần này, chúng ta sẽ xem về chuyện tương tác giữa `properties` và các `objects`. Đây là lúc `methods` xuất hiện, **`methods`** là một nhóm các statements (câu lệnh) thực hiện một số hoạt động (operations) và có thể trả về (return) hoặc không trả về một kết quả.

Có 3 loại `method` trong Python:

1. **Instance methods**
2. **Class methods**
3. **Static methods**

> Chúng ta sẽ gọi **method** để nói tới **instance method** vì nó thường được sử dụng nhất.

## Instance Method

### `self`

Ở những phần code ở trên, chúng ta thấy từ khóa `self` hay được xuất hiện, đây là lúc giải thích về nó. Đầu tiên, chúng ta cùng xem cách `self` argument hoạt động thông qua phần code bên dưới. Chúng ta có một class `Employee` như sau:

```python
class Employee:
    def __init__(self, ID=None, department=None):
        self.ID = ID
        self.department = department
```

Khi chúng ta tạo object employee1

```python
employee1 = Employee("Phu27", "FAA")
```

Thì Python sẽ convert giúp chúng ta thành:

```Python
Employee.__init__(employee1, "Phu27", "FAA")
```

Và bên trong `initializer` sẽ thực thi như sau:

```terminal
employee1.ID = "Phu27"
employee1.department = "FAA"
```

`self` parameter là một tham chiếu đến object hiện tại của class, và được sử dụng để truy cập các variables và methods thuộc về class.

Nó không nhất thiết phải được đặt tên là self, nó không phải là Python keyword, bạn có thể đặt nó là gì tùy thích, nhưng hầu hết chúng ta đều đặt nó là self, và bạn chẳng có lý do gì để đổi nó cả, và nó phải là parameter đầu tiên của initializer. Nếu không sẽ xảy ra lỗi:

```python
class Employee:
    def __init__(ID=None, department=None):
        ID = ID
        department = department


steve = Employee(3789, "Human Resources")

print(steve.ID)
print(steve.department)
```

Output

```terminal
Traceback (most recent call last):
  File "/Users/abre/Desktop/object-oriented-trong-python/test.py", line 7, in <module>
    steve = Employee(3789, "Human Resources")
TypeError: __init__() takes from 0 to 2 positional arguments but 3 were given
```

## Class Method trong Python

**Class methods** làm việc với **class variables** và có thể truy cập bằng cách sử dụng `Class name` thay vì object. Class method có thể được truy cập bằng cách sử dụng tên class mà không cần tạo class object.

### Syntax của class method

Để khai báo một class method, chúng ta sử dụng `@classmethod` decorator. `cls` parameter được sử để refer tới class cũng như chúng ta sử dụng `self` để refer tới object của class. Bạn cũng có thể sử dụng bất cứ tên nào để thay thế `cls`, nhưng vì quy ước (convention), chúng ta sẽ sử dụng `cls`.

> Tất cả class methods phải có ít nhất 1 parameter, là `cls`.

### Ví dụ class method

```python
class Player:
    team_name = 'Manchester City'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    # define class method get_team_name sử dụng @classmethod decorator
    @classmethod
    def get_team_name(cls):
        return cls.team_name


print(Player.get_team_name())
```

Output

```terminal
Manchester City
```

## Static methods trong Python

Static method là method được dùng chỉ giới hạn ở phạm vi class. Chúng không tương tác với **class variable** hay **instance variable**. Chúng được sử dụng như các _utility functions_ bên trong class.

> Static methods có thể được truy cập bằng cách sử dụng class name hoặc object name

### Syntax của static method

Để khai báo static method, chúng ta sử dụng `@staticmethod` decorator. Vì nó không được sử dụng để tham chiếu đến _object_ hay _class_ nên chúng ta không sử dụng `self` hay `cls` argument. Static methods không biết bất cứ thứ gì về state của class.

```python
class Player:
    team_name = 'Manchester City'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player('lol')
p1.demo()
Player.demo()

```

Output

```terminal
I am a static method.
I am a static method.
```

### Ví dụ static method

Giả sử chúng ta có 1 class `BodyInfo` chứa thông tin về cân nặng và chiều cao của một người. Chúng ta có thể tạo một static method để tính BMI cho bất kỳ `cân nặng` và `chiều cao` nào được truyền vào, ví dụ:

```python
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)

weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
```

Output

```terminal
23.148148148148145
```

Vì sự đặc biệt của static method, nó được dùng rất hạn chế, khi cần sử dụng utility function mà không cần tham chiếu tới object hay class thì chúng ta có thể tạo ra chúng, việc gọi chúng thông qua `class name` hay `class object` giúp chúng ta hiểu rõ về bối cảnh sử dụng cũng như chức năng của chúng.

# Access Modifiers trong Python

Chúng ta cùng tìm hiểu về `private`, `public` **attributes** trong Python

## Public attributes trong Python

Trong Python, tất cả _attributes_ mặc định là public. Nếu chúng ta muốn chỉ định một method hay variables nào đó không nên được coi là `public`, chúng ta phải khai báo nó là `private`.

### Ví dụ về public attributes

```Python
class Employee:
    def __init__(self, ID, salary):
        # các properties này đều là public
        self.ID = ID
        self.salary = salary

    # method này là public
    def display_id(self):
        print("ID:", self.ID)


steve = Employee(3789, 2500)
steve.display_id()
print(steve.salary)
```

Ouput

```terminal
ID: 3789
2500
```

Ở phần code trên, properties `ID`, `salary` và method `display_id()` là **public** nên chúng ta có thể truy cập ở trong cũng như ở ngoài class.

## Private attributes trong Python

Mục đích sử dụng private attributes là để ẩn nó khỏi người dùng và các class khác.

Nhưng trong Python, không có sự tồn tại của "private". Tuy nhiên, một quy ước đang được hầu hết các developer sử dụng là chúng ta có thể tạo private attributes bằng cách sử dụng tiền tố (prefix) `__`.

### Phân biệt giữa single leading underscore `_` và double leading underscores `__` trong Python

Hãy xem đoạn code dưới đây:

```python
class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

mc = MyClass()
```

```python
print(mc._semiprivate)
```

```terminal
, world!
```

```python
print(mc.__superprivate)
```

```terminal
Traceback (most recent call last):
  File "/Users/abre/Desktop/object-oriented-trong-python/test.py", line 10, in <module>
    print(mc.__superprivate)
AttributeError: 'MyClass' object has no attribute '__superprivate'
```

Single leading underscore `_` đơn giản chỉ là quy ước, một cách để lập trình viên chỉ ra rằng attributes này là private, không nên truy cập ngoài class này.

Double leading underscores `__` thì có ý nghĩa thật sự, trình thông dịch Python sẽ thay thế `__` bằng tên class mà gọi nó để đảm bảo attributes này sẽ không trùng với attributes khác có cùng tên trong class khác.

Tại sao ở trên mình nói trong Python, không có private, đoạn dưới sẽ giải thích.

### Private properties trong Python

Đầu tiên chúng ta xem khi truy cập vào một private property bằng cách thông thường sẽ như thế nào nhé:

```python
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary là một private property


steve = Employee(3789, 2500)
print("ID:", steve.ID)
print("Salary:", steve.__salary)  # dòng này sẽ gây lỗi
```

Output

```terminal
ID: 3789


Traceback (most recent call last):
  File "main.py", line 9, in <module>
    print("Salary:", steve.__salary)  # this will cause an error
AttributeError: 'Employee' object has no attribute '__salary'
```

`ID` là public property nhưng `__salary` là private property nên không thể truy cập bên ngoài class.

### Private methods trong Python

Truy cập vào private properties một cách thông thường sẽ gây lỗi, vậy với private methods thì sao?

```python
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary là một private property

    def display_salary(self):  # display_salary là một public method
        print("Salary:", self.__salary)

    def __display_id(self):  # display_id là một private method
        print("ID:", self.ID)


steve = Employee(3789, 2500)
steve.display_salary()
steve.__display_id()  # dòng này sẽ gây lỗi
```

Output

```terminal
Salary: 2500

Traceback (most recent call last):
  File "main.py", line 15, in <module>
    steve.__display_id()  # this will generate an error
AttributeError: 'Employee' object has no attribute '__display_id'
```

Tương tự như trên, `__display_id` là private method, không thể truy cập được từ bên ngoài class.

## Truy cập private attributes trong main code

Vậy tại sao ở trên nói trong Python không có sự tồn tại của "private"? Vì ta vẫn có cách truy cập các private attributes đó.

Nếu cảm thấy thật sự cần thiết sử dụng `private` property hoặc method, chúng ta... vẫn có thể. Ta sử dụng prefix `_<ClassName>` để truy cập, ví dụ như:

```python
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary là một private property

steve = Employee(3789, 2500)
print(steve._Employee__salary)  # truy cập private property
```

Output

```terminal
2500
```

Không có lỗi gì, chúng ta đã truy cập được `salary` của `steve` và in giá trị của nó ra, tương tự ta có thể dùng cách trên để truy cập private methods.

# Information Hiding trong Python

**Information hiding** là một khái niệm thiết yếu trong OOP. Nói một cách đơn giản thì để đảm bảo rằng dữ liệu được truy cập và sử dụng đúng mục đích và an toàn (bảo mật) thì chúng ta sẽ giấu đi các hoạt động bên trong class và chỉ cung cấp một giao diện (interface) mà qua đó thế giới bên ngoài có thể tương tác với class mà không cần biết điều gì đang xảy ra bên trong.

Data hiding có thể chia làm 2 phần chính:

1. Encapsulation (Tính đóng gói)
2. Abstraction (Tính trừu tượng)

## Encapsulation (Tính đóng gói) trong Python

Encapsulation (tính đóng gói) là một kỹ thuật lập trình cơ bản được sử dụng để ẩn dữ liệu trong OOP. Có thể hiểu, tính đóng gói là việc giấu tất cả dữ liệu, methods vào bên trong và chúng ta sẽ thao tác với dữ liệu, methods đó bên trong class. Những thứ bên trong sẽ không thể bị sửa đổi hay truy cập bởi codes bên ngoài từ các nơi khác của chương trình.

### Getter and Setters trong Python

> Như vài ngôn ngữ lập trình khác, để có thể truy cập vào các private properties từ bên ngoài class, chúng ta dùng `getter` và `setter`

- `getter` method cho phép đọc giá trị của property
- `setter` method cho phép chỉnh sửa giá trị của property

Trong Python cũng có thể sử dụng getter, và setter.

```python
class User:
    def __init__(self, username=None):
        self.__username = username

    def set_username(self, x):
        self.__username = x

    def get_username(self):
        return (self.__username)


steve = User('steve1')
print('Before setting:', steve.get_username())
steve.set_username('steve2')
print('After setting:', steve.get_username())

```

Output

```terminal
Before setting: steve1
After setting: steve2
```

Ở đoạn code trên, chúng ta đã tạo một class `User`, 1 private property `username` và getter và setter method cho property đó. Sau đó chúng ta tạo object `steve` và gán giá trị của `username` là "steve1", sau đó in ra giá trị đó. Tiếp theo đó chúng ta sử dụng `set_username` method để thay đổi giá trị của `username` thành "steve2" sau đó chúng ta thấy giá trị của `username` đã được sửa thành "steve2" khi in ra.

### `@property` decorator

Sau khi tìm hiểu cách Python sử dụng getter setter thì... quên những gì bạn vừa đọc đi, đã có nhiều [thảo luận](https://stackoverflow.com/questions/2579840/do-you-use-the-get-set-pattern-in-python) về việc dùng `getter, setter` trong Python và đa số người sử dụng Python đều không sử dụng nó. Tóm tắt là nó rối, nó tốn tài nguyên, và Python được sinh ra để trở thành ngôn ngữ lập trình dễ sử dụng cho con người.

Thay vào đó họ sử dụng [`@property`](https://docs.python.org/3/library/functions.html#property) decorator nếu như muốn "làm gì đó `private`" với attributes trong class. Trong bài học của khóa học [CS50P](https://cs50.harvard.edu/python/2022/) họ cũng sử dụng decorator này.

Giờ tìm hiểu về nó nhé.

`@property` decorator

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.__name = name
        self.__house = house

    def __str__(self):
        return f"{self.__name} from {self.__house}"

    # Getter cho house
    # Hãy chắc chắn rằng tên của getter và setter trùng với tên của property
    @property
    def house(self):
        return self.__house

    # Setter cho house
    # Hãy chắc chắn rằng tên của getter và setter trùng với tên của property
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.__house = house


def main():
    # Ở đây mình sẽ nhập name là Abre, house là: Hufflepuff
    student = get_student()
    print(f"Student info: {student}")
    print(student)
    # Truy cập house của student
    print(f"House of student: {student.house}")
    # Thay đổi giá trị của house của student thành Ravenclaw
    student.house = "Ravenclaw"
    # In ra thông tin student sau khi đổi
    print(f"Student info after change house: {student}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

Output

```terminal
Name: Abre
House: Hufflepuff
Student info: Abre from Hufflepuff
House of student: Hufflepuff
Student info after change house: Abre from Ravenclaw
```

Như ở trên, ta có thể thấy `@property` được sử dụng để lấy giá trị của thuộc tính private mà không cần sử dụng bất kỳ phương thức getter nào. Chúng ta thêm một dòng `@property` trước method mà chúng ta trả về private variable. Còn để set giá trị cho private variable, chúng ta thêm dòng `@method_name.setter` trước method đó rồi sử dụng nó như một setter.

Bạn có thể tìm hiểu thêm tại [đây](https://www.datacamp.com/tutorial/property-getters-setters) và [oop lecture from CS50P](https://cs50.harvard.edu/python/2022/notes/8/).

### Lợi ích của Encapsulation trong Python

- Dễ bảo trì: Code được đóng gói trong những phần riêng biệt, như là class, interface, v.v... Vì vậy khi thay đổi hay cập nhật thì chúng không ảnh hưởng đến phần còn lại.
- Testing khỏe hơn: Chúng ta dễ test hơn vì sẽ chỉ phải tập trung ở 1 nơi chứ không phải lo nó còn ảnh hưởng đến nơi nào khác không. Tiết kiệm thời gian.
- Che giấu dữ liệu: Khi sử dụng người dùng chỉ sẽ nhận được kết quả mà không biết hay truy cập được chi tiết bên trong của object.

# Inheritance (tính kế thừa) trong Python

Inheritance giúp tăng khả năng tái sử dụng code bằng cách cung cấp cho chúng ta cách để tạo một class mới từ một class hiện có. Class mới (class con/**child class**) sẽ kế thừa tất cả các non-private attributes (chỉ cần không phải private thì đều được kế thừa) từ class hiện có (class cha/**parent class**).

Vậy, khi nào ta sử dụng inheritance?

Bất cứ khi nào mối quan hệ giữa 2 objects là **IS A** thì chúng ta có thể. Ví dụ như `Car` **IS A** `Vehicle`, `Bicycle` **IS A** Vehicle, v.v... `Vehicle` sẽ có các properties như `make`, `color`, `model`.

`Car` hay `Bicycle` hay `Train` đều có các properties trên, và chúng đều **IS A** `Vehicle`.

Giả sử phần mềm chúng ta được tạo ra để quản lý `Vehicle`. Chúng ta sẽ tạo ra class `Vehicle` và nó sẽ là parent class (super class), `Car` hay `Bicycle` hay `Train` sẽ là child class (sub class) và chúng sẽ thừa kế từ `Vehicle` các **non-private** attributes.

## Triển khai inheritance trong Python

```python
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # gọi constructor (initializer) từ parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def print_car_details(self):
        self.print_details()
        print("Doors:", self.doors)


suzuki1 = Car("Suzuki", "Grey", "2015", 4)
suzuki1.print_car_details()
```

Output

```terminal
Manufacturer: Suzuki
Color: Grey
Model: 2015
Doors: 4
```

Ở đoạn code trên, chúng ta tạo ra 2 class `Vehicle` - parent class và `Car(Vehicle)` - child class thừa kế từ `Vehicle`.

Như đã nói, child class sẽ thừa kế lại các non-private methods và variables từ parent class. Chúng ta tạo ra object Car `suzuki1` và truyền vào giá trị cho nó. Sau đó chúng ta gọi hàm `print_car_details` và hàm này đã in ra toàn bộ thông tin của `suzuki1` mà trong đó có sử dụng hàm `print_details` của `Vehicle`.

Để ý hàm `__init__` của `Car`, chúng ta có gọi lại hàm `__init__` của `Vehicle`, hàm `print_car_details` cũng gọi hàm `print_details` của `Vehicle`.

## `super()` function

Việc sử dụng `super()` phát huy tác dụng khi chúng ta triển khai inheritance. Nó được sử dụng trong child class để tham chiếu đến attributes của parent class mà không cần đặt tên rõ ràng cho các methods, variables.

Nó làm cho codes dễ quản lý hơn và không cần dùng tên của parent class để truy cập các attributes của parent class.

### Sử dụng super() function truy cập vào property của parent class

```python
class Vehicle:
    fuel_cap = 90

class Car(Vehicle):
    fuel_cap = 50

    def display(self):
        # truy cập fuel_cap từ class Vehicle dùng super()
        print("Fuel cap from the Vehicle Class:", super().fuel_cap)

        # truy cập fuel_cap từ class Car dùng self
        print("Fuel cap from the Car Class:", self.fuel_cap)


obj1 = Car()  # tạo một car object
obj1.display()  # gọi method display() của class Car
```

Output

```terminal
Fuel cap from the Vehicle Class: 90
Fuel cap from the Car Class: 50
```

Chúng ta đã truy cập vào giá trị của property `fuel_cap` của parent class bằng cách sử dụng `super().`parent_class_property.

### Gọi method của parent class

```python
class Vehicle:
    def display(self):
        print("I am from the Vehicle Class")


class Car(Vehicle):
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()
obj1.display()  # gọi method display() của class Car
```

Output

```terminal
I am from the Vehicle Class
I am from the Car Class
```

Ta có thể thấy, `super()` đã tham chiếu đến parent class và truy cập vào `display()` method ở parent class.

### Sử dụng `super()` với initializer

```python
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
```

Ở phần code đầu tiên giới thiệu về inheritance, chúng ta gọi `__init__` bằng tên của parent class

```python
ParentClass().__init__(a, b)
```

Ở đây lại gọi `__init__` bằng `super()`, đó là 2 cách chúng ta có thể.

Như đã nói, child class thừa kế tất cả non-private attributes của parent class. Chúng ta có thể dùng `self` để truy cập chúng. Và chúng ta đã gọi `self.print_details` ở phần [Triển khai inheritance trong Python](#triển-khai-inheritance-trong-python) thay vì `super().print_details` là tại vì ở ví dụ đó, chúng ta có 2 methods _khác tên_ (`print_car_details` và `print_details`).

Nếu chúng ta dùng `self` mà tên 2 methods ở parent class và child class là giống nhau thì sẽ bị lỗi. Còn ở [ví dụ này](#gọi-method-của-parent-class) chúng ta có thể đặt tên method của parent class và child class giống nhau vì chúng ta dùng `super()` để gọi method từ parent class, tiện thể nhắc luôn parent class còn được gọi là super class.

### Lợi ích của Inheritance

#### Reusability (Tái sử dụng)

Ví dụ như sau, ta có một ứng dụng dành cho ngân hàng, ta thiết kế class `BankAccount` và cho class `SavingsAccount` và class `CheckingAccount` thừa kế `BankAccount`, và cả 2 loại account này đều có behaviors như `deposit()` và `withdraw()` nên ta đưa 2 methods này vào class `BankAccount` luôn.

Trong ví dụ trên chúng ta không cần viết lại code cho 2 methods `deposit()` và `withdraw()` bên trong 2 child classes `SavingsAccount` và `CheckingAccount`.

#### Code modification (Dễ bảo trì/ sửa đổi)

Giả sử bạn đặt cùng một đoạn code vào các class khác nhau, khi chúng ta muốn sửa đổi đoạn code đó, và nó ở trong rất nhiều class, sẽ có khả năng chúng ta quên sửa ở 1 class nào đó và sẽ dẫn đến lỗi.

Chúng ta có thể tránh việc này bằng cách sử dụng inheritance, thứ sẽ đảm bảo việc sửa đổi ở parent class sẽ được diễn ra ở child class.

#### Extensibility (Khả năng mở rộng)

Ví dụ sau này chúng ta muốn tạo 1 class mới cho ứng dụng ngân hàng này, gọi nó là `MoneyMarketAccount` thì chúng ta có thể thừa kế lại từ `BankAccount` class thay vì implement một class từ đầu vì chúng ta có thể sử dụng các attributes phổ biến của `BankAccount` cho `MoneyMarketAccount`.

#### Data hiding (Che giấu dữ liệu)

Parent class giữ một số dữ liệu private vì vậy child class không thể thay đổi nó. Như hình trên, người dùng sử dụng các methods trên mà không cần biết bên trong nó là gì, và cũng không thể sửa đổi các private variables của object.

# Polymorphism (Tính đa hình) trong Python

## Dẫn nhập về tính đa hình trong Python

### Dẫn nhập 1

Trong lập trình, polymorphism để cập đến việc cùng 1 object thể hiện các hành vi khác nhau.

Ví dụ: hình tròn (circle), hình vuông (square) đều là hình (shape) nhưng properties của chúng là khác nhau. Đa hình là vậy.

Giả sử ứng dụng của chúng ta cần method để tính diện tích của từng shape cụ thể. Công thức tính diện tích của mỗi hình là khác nhau, nên chúng ta không thể cung cấp 1 method duy nhất mà sử dụng cho 2 shapes trên được. Chúng ta có thể tạo ra các methods riêng biệt trong từng class (ví dụ `get_square_area()`, `get_circle_area()`, etc.) Nhưng làm vậy sẽ khó để nhớ _methods name_ vì có rất nhiều shapes.

Sẽ tốt hơn nếu methods tính diện tích của các shapes đều là `get_area()`. Chúng ta sẽ dễ dàng sử dụng ứng dụng hơn. Có thể làm được điều này bằng cách sử dụng polymorphism trong OOP. **Parent class** sẽ define một methods mà không implement gì trong đó. Mỗi **child class** sẽ thừa kế methods đó và tự implement phù hợp cho riêng mình.

Class `Shape` sẽ có method `get_area()`, các child class như `Square`, `Circle` sẽ thừa kế lại method này. Khi `Square` gọi method `get_area()` thì sẽ phản hồi bằng cách gọi methods `get_area()` của `Square`, tương tự với class `Circle`, v.v...

### Dẫn nhập 2

Sư tử (Lion), chó (Dog), gà (Chicken) đều là động vật (Animal), nhưng properties của chúng thì không giống nhau hoàn toàn. Lấy ví dụ theo trên, ta có class `Animal` và các class `Lion`, `Dog`, `Chicken` sẽ kế thừa class `Animal`.

Class `Animal` sẽ có các methods, ví dụ ở class `Animal` chúng ta có method tạo ra tiếng ồn (`make_noise`), các class kế thừa từ `Animal` cũng sẽ có method này, việc triển khai method này trên các con vật khác nhau sẽ khác nhau. Ví dụ con chó, con gà, và sư tử, chúng đều là Animal nhưng tiếng động chúng phát ra là khác nhau.

## Triển khai tính đa hình (polymorphism) sử dụng tính kế thừa (inheritance) trong Python

```python
class Shape:
    def __init__(self):
        pass

    def get_area(self):
        pass

# class Rectangle thừa kế từ class Shape
class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # method get_area() của Rectangle
    def get_area(self):
        return (self.width * self.height)

# class Circle thừa kế từ class Shape
class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    # method get_area() của Circle
    def get_area(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].get_area()))
print("Area of circle is:", str(shapes[1].get_area()))
```

Output

```terminal
Area of rectangle is: 60
Area of circle is: 153.958
```

Chúng ta tạo ra class `Shape` với một public method `get_area()`, class `Rectangle` và class `Circle` thừa kế lại từ class `Shape`. Chúng thừa kế lại method `get_area()` của class `Shape` nhưng `get_area()` của mỗi class sẽ trả về giá trị diện tích của mỗi class, không giống nhau.

Đây gọi là polymorphism: các methods giống nhau nhưng sẽ triển khai cụ thể cho từng class.

## Method overriding (ghi đè phương thức) trong Python

Trong OOP, nếu một child class implement lại một method đã được định nghĩa (define) ở parent class, thì nó được gọi là method overriding.

Như ví dụ ở trên, là _method overriding_.

Giả sử ta có một parent class `Animal` và child class `Lion`. Cả hai đều có method `print_animal`, method này có cùng tên, cùng parameters, và cùng return type. Nhưng nội dung được triển khai (implementation) bên trong thì khác nhau.

### Ví dụ về method overriding

```python
class Animal:
  def __init__(self):
    pass

  def print_animal(self):
    print("I am from the Animal class")

  def print_animal_two(self):
    print("I am from the Animal class")


class Lion(Animal):
  def __init__(self):
    super()

  def print_animal(self): # method overriding
    print("I am from the Lion class")


lion = Lion()
lion.print_animal()
lion.print_animal_two()
```

Khi chạy chương trình thì chúng ta sẽ nhận được:

```terminal
I am from the Lion class
I am from the Animal class
```

### Lợi ích của Method overriding

- Child class có thể tự triển khai method của riêng chúng với các method đã thừa kế từ parent class mà không cần sửa đổi method ở parent class.
- Child class có thể sử dụng cách triển khai method của parent class hoặc định nghĩa lại cách triển khai của riêng nó.

## Method overloading (nạp chồng phương thức) trong Python

Khái niệm method overloading là hiện tượng nhiều method có cùng tên, tuy nhiên số lượng parameters hoặc type của parameters trong các methods này là khác nhau. Overloading đề cập đến việc làm cho một method thực hiện các hoạt động (operations) khác nhau dựa trên các arguments của nó. Tùy vào số lượng và kiểu của parameters truyền vào thì class sẽ biết mà xử lý để trả về các kết quả tương ứng.

> Các method có cùng tên, cùng danh sách parameters, nhưng kiểu trả về khác nhau không được xem là overloading method.

Không như các ngôn ngữ lập trình khác, ở Python thì methods **không thể** explicitly overloaded (nạp chồng rõ ràng), chỉ có thể implicitly overloaded (nạp chồng ngầm).

Như ở `Java` thì có thể tạo nhiều constructor trong class với số lượng parameters khác nhau để khi tạo object tùy số lượng parameters truyền vào thì Class sẽ biết mà sử dụng constructor nào.

Có 2 cách để tạo ra hiện tượng overload:

- Thay đổi số lượng tham số
- Thay đổi kiểu dữ liệu của tham số

```python
class Sum:
    def addition(self, a, b, c = 0):
        return a + b + c
```

Để hiểu rõ cái này mình sẽ thêm 1 ví dụ về Java ở đây:

```java
class Sum {
  // addition 1
  public int addition(int a, int b) {
    return a + b;
  }
  // addition 2
  public int addition(int a, int b, int c) {
    return a + b + c;
  }
}
```

Ta thấy ví dụ ở Java, ta có 2 methods cùng tên `addition`, khi ta gọi method này với _số lượng parameter là 2_ thì sẽ nhận được kết quả từ method `addition 1`, còn _số lượng parameter truyền vào là 3_ thì sẽ nhận được kết quả từ method `addition 2`.

Thêm một ví dụ rõ hơn trong Python

```python
class Employee:
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def demo(self, a, b, c):
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)


# Tạo object steve của class Employee
steve = Employee()

# In ra properties của object steve
print("Demo 1")
steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
steve.demo(1, 2, 3, 4, 5)

```

Output

```terminal
Demo 1
a =  1
b =  2
c =  3


Demo 2

Traceback (most recent call last):
  File "main.py", line 30, in <module>
    steve.demo(1, 2, 3, 4, 5)
TypeError: demo() takes 4 positional arguments but 6 were given
```

Nhận được `TypeError`, điều này là khi có nhiều method trùng tên, Python sẽ coi method được khai báo cuối cùng là method sẽ được sử dụng khi chúng ta gọi. Ở đây là method `demo` với 4 parameters nên khi ta truyền vào 5 parameter, tính cả instance là 6 nên nó đã báo lỗi.

Vậy phải làm sao? Chúng ta có vài cách để thực hiện method overloading trong Python, ở đây chúng ta sẽ dùng **multiple dispatch**

#### `Multipledispatch trong Python`

```python
from multipledispatch import dispatch

class Employee:
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    @dispatch(int, int, int, int, int)
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    @dispatch(int, int, int)
    def demo(self, a, b, c):
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)

# Tạo object steve của class Employee
steve = Employee()

# In ra properties của object steve
print("Demo 1")
steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
steve.demo(1, 2, 3, 4, 5)
```

Output

```terminal
Demo 1
a =  1
b =  2
c =  3


Demo 2
a = 1
b = 2
c = 3
d = 4
e = 5
```

Dựa vào `multipledispatch` chúng ta đã overloading method một cách rõ ràng, như cách nó xảy ra ở Java.

## Operator overloading (nạp chồng toán tử) trong Python

Toán tử (operator) trong Python có thể được overloaded để hoạt động theo một cách nhất định dựa trên người dùng.

> Java và JavaScript không hỗ trợ operator overloading.

Bất cứ khi nào một toán tử được sử dụng trong Python, method tương ứng sẽ được gọi để thực function đã define trước đó của nó.

Ví dụ khi sử dụng toán tử `+`, nó sẽ gọi hàm đặc biệt `__add__`.

Trong Python, toán tử `+` nếu được sử dụng giữa hai `int` data types chúng sẽ cộng hai số lại với nhau. Còn khi toán tử này được sử dụng với hai `string` data types chúng sẽ merge hai chuỗi đó lại với nhau.

### Overloading operators cho một class do người dùng định nghĩa

```python
class Character:
    def __init__(self, name, strength=0, agility=0, intellect=0):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intellect = intellect

    def __str__(self):
        return f"{self.name} has {self.agility} strength, {self.intellect} agility and {self.intellect} intellect"

    def __add__(self, other):
        name = self.name + other.name
        strength = self.strength + other.strength
        agility = self.agility + other.agility
        intellect = self.intellect + other.intellect
        return Character(name, strength, agility, intellect)


hammer = Character("Hammer", 10,  50, 25)
print(hammer)

wolf = Character("Wolf", 50, 10, 10)
print(wolf)

polymerization = hammer + wolf
print(polymerization)
```

Output

```terminal
Hammer  has 50 strength, 25 agility and 25 intellect
Wolf  has 10 strength, 10 agility and 10 intellect
HammerWolf  has 60 strength, 35 agility and 35 intellect
```

Ở trên, mình đã overloaded lại operator `+`, và sử dụng trong class Character với 2 character `hammer` và `wolf`, và đã dung hợp (polymerization) chúng nó lại để thành 1 character khác.

> Bạn có thể đặt tên argument thứ hai là bất cứ gì, nhưng theo quy ước thì chúng ta sẽ sử dụng `other` để nói tới other object.

## Triển khai tính đa hình (polymorphism) sử dụng `duck typing` trong Python

Duck Typing là 1 đặc trưng của các ngôn ngữ động như Python, nó được coi là một trong những concepts hữu ích nhất trong OOP trong Python, nó được dùng khi type hoặc class của object không quan trọng bằng method mà nó triển khai.

Tên gọi bắt nguồn từ _duck test_ với tư tưởng: "Nếu ta thấy 1 con vật đi 2 chân và biết bơi như con vịt thì đấy hẳn là con vịt". Duck typing kế thừa và phát triển lại từ khái niệm **dynamic typing** trong Python, dynamic typing có nghĩa là chúng ta có thể thay đổi _type_ của object sau khi chúng được tạo ra.

Đoạn code sau biểu hiện dynamic typing trong Python

```python
x = 5  # type of x là integer
print(type(x))

x = "Educative"  # type of x giờ là string
print(type(x))
```

Output

```terminal
<class 'int'>
<class 'str'>
```

Giờ ta triển khai duck typing

```python
class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)
```

Output

```terminal
Woof woof
Meow meow
```

Type của `Animal` sẽ được xác định khi method được gọi, nên không quan trọng là `Dog` hay là `Cat` miễn là method `Speak()` phải được định nghĩa trong 2 class đó.

Đây là cách chúng ta triển khai polymorphism mà không cần inheritance. Vì có là `Dog` hay `Cat` cũng không quan trọng, chúng đều thuộc nhóm đối tượng `Animal`, và có các hành vi gần như nhau `Speak()`. Ở phần dưới sau khi tìm hiểu về tính trừu tượng, chúng ta sẽ dễ hiểu hơn.

# Tính trừu tượng (Abstraction) và Abstract Base Class trong Python

Đầu tiên mình muốn nói về tính trừu tượng, nó được sử dụng để ẩn tất cả quy trình và dữ liệu không liên quan của ứng dụng. Đối với người dùng, những thông tin đó không cần thiết. Việc này giúp tăng hiệu quả sử dụng của phần mềm (giảm độ phức tập).

Ví dụ chúng ta rút tiền ở máy ATM, ta điền số tiền muốn rút vào và chỉ cần thoả điều kiện là số tiền muốn rút nhỏ hơn số dư trong tài khoản là ta có thể rút tiền được, tiền sẽ chạy ra ở khe máy.

Chúng ta không cần quan tâm máy làm cách nào để đưa tiền ra hay cách máy kiểm tra số tiền muốn rút và số dư trong tài khoản bằng cách nào.

Tiếp theo mình muốn nói về `interface` và mượn ví dụ từ ngôn ngữ lập trình _Java_ để chúng ta dễ hình dung về abstract base class. Interface sẽ định nghĩa các hành vi (behaviors) của một nhóm đối tượng đó. Ví dụ: Một con chó (con vật) thì có các behaviors như: chạy, ngủ, sủa, v.v...

```java
interface DogBehaviors {
    // Method chạy với tham số tốc độ (speed)
    void run(int speed);
    // Method sủa với tham số là số lần (n)
    void bark(int n);
    // Method ngủ
    void sleep();
}
```

Sau này khi tạo ra một con chó, dù nó là loại chó nào thì nó cũng sẽ có các hành vi trên

```java
class Dog implements DogBehaviors {
    // Method chạy với tham số tốc độ (speed)
    void run(int speed) {
        ...
    }
    // Method sủa với tham số là số lần (n)
    void bark(int n) {
        ...
    }
    // Method ngủ
    void sleep() {
        ...
    }
}
```

Một `interface` sẽ khai báo ra các methods của nó, các methods này không có nội dung cụ thể (gọi là abstract method). Class mà implements **interface** này phải có tất cả các methods được khai báo trong **interface** và phải định nghĩa nội dung của methods.

Như vậy, `interface` và `class` là hai khái niệm khác nhau. **Interface** định nghĩa ra 1 tiêu chuẩn nào đó mà các class implement nó phải tuân thủ.

Trong Python thì không có interface, nên tính trừu tượng trong Python được triển khai nhờ vào Abstract Base Class. Abstract Base Class (ABC) định nghĩa một tập hợp các properties và methods mà 1 class phải implement.

## Tại sao phải dùng ABC?

Xem ví dụ sau đây:

```python
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
square = Square(4)
```

Ta có thể thấy object `shape` có thể được tạo ra mặc dù object này không có gì cả. Để ngăn cản user tạo object từ class `Shape`, chúng ta dùng `ABC`.

## Syntax của Abstract Base Class trong Python

Để định nghĩa một ABC, chúng ta sử dụng module `abc`. Abstract base class được kế thừa từ built-in class `ABC`. Chúng ta phải sử dụng decorator `@abstractmethod` phía trên method mà chúng ta muốn khai báo là một phương thức trừu tượng (abstract method).

Lưu ý rằng các `abstractmethod` trong parent class thì ta không được triển khai nó, mà chỉ được định nghĩa nó để child class kế thừa lại và triển khai.

```python
from abc import ABC, abstractmethod

class ParentClass(ABC):

    @abstractmethod
    def method(self)
```

### Ví dụ 1 về abstract base class

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Shape là child class của class ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

shape = Shape()
```

Output

```terminal
Traceback (most recent call last):
  File "main.py", line 19, in <module>
    shape = Shape()
TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

Đoạn code trên không compile được vì khi ta tạo ra object `shape`, ở class `Shape`, 2 abstract methods `area()` và `perimeter()` chưa được triển khai gì cả.

### Ví dụ 2 về abstract base class

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape là child class của class ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


square = Square(4)

```

Output

```terminal
Traceback (most recent call last):
  File "main.py", line 19, in <module>
    square = Square(4)
TypeError: Can't instantiate abstract class Square with abstract methods area, perimeter
```

Như có thể thấy, code cũng không compile được khi ta tạo object từ class `Square` vì chúng ta chưa định nghĩa cho hai abstract methods `area()` và `perimeter()` trong class `Square`. Giờ ta sẽ làm điều đó.

### Ví dụ 3 về abstract base class

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape là child class của class ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
```

Output

```terminal
Traceback (most recent call last):
  File "main.py", line 25, in <module>
    shape = Shape()
TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

Giờ ta đã định nghĩa cho hai abstract methods `area()` và `perimeter()` trong class `Square`. Nhưng ở class `Shape` thì 2 abstract methods đó vẫn chưa có gì, nên khi ta tạo object từ class `Shape` thì chương trình vẫn sẽ bị lỗi (như ví dụ 1), không compile được.

### Ví dụ 4 về abstract base class

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape là child class của class ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(4)
print("Square's area: {}".format(square.area()))
```

Output

```terminal
Square's area: 16
```

Giờ đã compile được, vì chúng ta đã implement ở 2 abstract methods của class `Square`. Như bạn có thể thấy, cùng đoạn code ở `ví dụ 3 về abstract base class` nhưng ta không thể tạo ra object của class `Shape` nhưng `Square` thì có thể.

> Methods với `@abstractmethod` decorators ở parent class phải được triển khai ở child class.

Việc dùng ABC, chúng ta có thể quản lý objects nào được tạo và không được tạo.
