class student:
    def_int_(self,name,
roll_number,cgpa):
         self.name=name
         self.roll_number
=roll_number
         self.cgpa=cgpa
def
sort_students(students_list):
sorted_students=sorted(stude
nt_list,key=lambda student:
student.cgpa,reverse=true)
        return
sorted_students
students=[students("Alice","AOO
1",3.8),
           student
("Bob","BOO2",3.6),
              student
("Charlie","DOO4",3.7)]
#sort the students by CGPA
sorted_students=sort_student
s(students)
#print the sorted list for
student in sorted_students
    print("Name:{student
name},Roll Number:
{student.roll_number},CGPA:
{student cgpa}")
              
