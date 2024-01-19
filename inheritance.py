class user:
    #defining the attributes of the parent class
    fname = "First Name"
    lname = "Last Name"
    email = "email@email.com"

class Student(user):
    #attributes of child class "Student"
    gpa = 3.5
    major = "Computer Science"

class Instructor(user):
    #attributes of child class "Instructor"
    department = "Mathematics"
    salary = 50,000


