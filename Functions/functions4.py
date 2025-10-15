def student_details(name: str, age: int, cgpa: float) -> int:
    print("Student name is", name)
    print("Student age is", age)
    print("Student CGPA is", cgpa)
    return name, age

returnn = student_details("pradeep", 20, 8.9)
print("return name is :", returnn)

def student_details(name, age, cgpa):
    print("student details : ")
    print("Name", name)
    print("age",age)
    print("cgpa", cgpa)
    return age

age_return = student_details("pradeepkumar b c", 21, 9.0)
print("the return age is : ", age_return)