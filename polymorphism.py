class user:
    #defining the attributes of the parent class
    fname = "John"
    lname = "Doe"
    email = "doe@gmail.com"

    #this method welcomes back users or lets them know its incorrect
    def UserLogin(self):
        login_name = input("Enter your first name: ")
        login_email = input("Enter your email: ")
        if (login_name == self.fname and login_email == self.email):
            print("Welcome back, {}!".format(login_name))
        else:
            print("Error: incorrect name and email")

class Student(user):
    #attributes of child class "Student"
    gpa = 3.5
    major = "Computer Science"
    student_ID = "9876"

    #similar method to the userLogin but asks for student ID
    def UserLogin(self):
        login_name = input("Enter your first name: ")
        login_ID = input("Enter your Student ID: ")
        if (login_name == self.fname and login_ID == self.student_ID):
            print("Your GPA is {}, and your major is {}!".format(self.gpa,self.major))
        else:
            print("Invalid login credentials!")

class Instructor(user):
    #attributes of child class "Instructor"
    department = "Mathematics"
    employee_ID = "1234"

    #creates a method that requires employee ID
    def UserLogin(self):
        login_name = input("Enter your first name: ")
        employee_ID = input("Enter your Employee ID: ")
        if (login_name == self.fname and employee_ID == self.employee_ID):
            print("You teach {} classes!".format(self.department))
        else:
            print("Invaid login credentials!")

#This calls the functions we created for the user, student, and instructor
user1 = user()
user1.UserLogin()

student1 = Student()
student1.UserLogin()

employ1 = Instructor()
employ1.UserLogin()
