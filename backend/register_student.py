from student_service import add_student

print("-----------------------------")
print("Student Registration")
print("-----------------------------")

name = input("Enter Name: ")
email = input("Enter Email: ")

success = add_student(name, email)

if success:
    print("-----------------------------")
    print("Registration Completed")
    print("-----------------------------")