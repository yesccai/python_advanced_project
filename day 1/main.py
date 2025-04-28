from student import  Student
from teacher import Teacher

s = Student("Alice", 20, "S12345")
t =Teacher("Bob", 35, "T54321")

print(s.introduce())
print(t.introduce())

s1 = Student("Alice", 20, "S12345")
s2 = Student("Alice", 21, "S12345")
s3 = Student("Tom", 22, "S67890")

print(str(s1))
print(repr(s1))
print(s1 == s2)  # True
print(s1 == s3)  # False