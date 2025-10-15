def get_topper_name(schoolName: str, grade: int, subject: str):
    return "Ram"

student_name = get_topper_name("Navodaya", 5 , "Math")
print("Topper Student Name : ", student_name)



def get_school_name(schoolId: int) -> str:
    return "Navodaya"

school_name = get_school_name("navodaya")
print(school_name)



def get_boys_girls_count_for_grade_in_school(schoolId: int, grade: int) -> int:
    return 100, 100

boys_count, girls_count = get_boys_girls_count_for_grade_in_school(5,10)
print("Count for boys and girls : ", boys_count, girls_count)

