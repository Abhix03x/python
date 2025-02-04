

class Student:
    name=None
    mark1=0
    mark2=0

students = []


for i in range(2):
    s=Student()
    s.name = input('enter the name')
    s.mark1 = int(input("enter the mark1"))
    s.mark2 = int(input("enter the mark2"))
    students.append(s)

for st in students:
    print(f"Name:{st.name} Mark1:{st.mark1} Mark2:{st.mark2}")