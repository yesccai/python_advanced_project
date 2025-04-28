from person import Person

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def introduce(self):
        return f"I am {self.name}, a teacher. My ID is {self.teacher_id}."