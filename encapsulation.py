#protected access function
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _user(self):
        print("Name: ", self._name)
        print("Age: ", self._age)

class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age)
        self._id_number = id_number

    def user(self):
        self._user()
        print("Id Number: ", self._id_number)

#creates an object
obj = Student("Mary", 21, 4567)
#calling the function
obj.user()


#private access function
class PrivateInfo:
    def __init__(self, DOB, GPA):
        self.__DOB = DOB
        self.__GPA = GPA

    def __display_Info(self):
        print("Date of Birth:", self.__DOB)
        print("Grade Average:", self.__GPA)
        
    #access the private attribute
    def accessInfo(self):
        self.__display_Info()

obj = PrivateInfo(110289, 3.0)
#calling our function
obj.accessInfo()


