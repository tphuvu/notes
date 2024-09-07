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
