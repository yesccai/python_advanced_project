from person import Person

class Student(Person):
    def __init__(self,name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"I am {self.name}, a student. My ID is {self.student_id}."

    def __str__(self):
        return f"Student({self.name}, {self.age}, {self.student_id})"

    def __repr__(self):
        return f"Student(name = {self.name}, age = {self.age}, student_id = {self.student_id}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False