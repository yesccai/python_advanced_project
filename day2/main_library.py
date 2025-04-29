from library_system import Book, Student, Teacher, Library

lib = Library()
b1 = Book("Python入门", "张三")
b2 = Book("算法导论", "李四")

lib.add_book(b1)
lib.add_book(b2)

stu = Student("小明")
tch = Teacher("李老师")

print(stu.borrow_book(b1))
print(tch.borrow_book(b1))
print(tch.borrow_book(b2))