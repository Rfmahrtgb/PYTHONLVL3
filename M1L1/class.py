class Student:
    color = "color"
    student_nution = "nution"

    def go(self):
        print("Work")

    def stop(self):
        print("Rest")

    def info(self):
        print("цвет кожи: ", self.color, ", национальность: ", self.student_nution)

student = Student()

print(student.color)
print(student.student_nution)

student.color = "бежевый"
student.student_nution = "русский"

student.go()  
student.stop()  
student.info()
