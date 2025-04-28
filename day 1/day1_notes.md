---

# 📄 Day 1 学习笔记 —— Python 类、对象与特殊方法

---

## 1. 类与对象基础

### 什么是类（Class）

- 类是创建对象的模板，定义了对象的基本结构和行为（属性和方法）。
- 类通过关键字 `class` 来声明。
- 类本身是抽象的，实例化后才变成具体的对象。

### 什么是对象（Instance）

- 对象是类的具体实例。
- 对象拥有类中定义的属性和方法。
- 通过类名调用，使用括号传参实例化对象。

**示例：**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 20)
print(p1.name)  # Alice
print(p1.age)   # 20
```

---

## 2. 构造方法 `__init__`

- `__init__` 是类的初始化方法，在创建对象时自动调用。
- 主要用于定义对象的初始状态（赋初值给属性）。

**示例：**

```python
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
```

**理解要点：**
- `self` 代表实例本身（必须作为第一个参数）。
- `self.name = name` 把局部变量赋值给实例属性。

---

## 3. 方法（Method）

- 方法是定义在类内部的函数。
- 用来描述对象的行为（功能动作）。

**示例：**

```python
def introduce(self):
    return f"My name is {self.name}, and I am {self.age} years old."
```

对象调用方法：
```python
p = Person("Tom", 30)
print(p.introduce())
```

---

## 4. 特殊方法（Magic Methods）

### 4.1 `__str__`

- 用于定义对象被 `print()` 时的**用户友好字符串表示**。
- 目的是让输出更符合阅读习惯。

**示例：**
```python
def __str__(self):
    return f"Student({self.name}, {self.age}, {self.student_id})"
```
调用效果：
```python
print(s1)  
# 输出：Student(Alice, 20, S12345)
```

---

### 4.2 `__repr__`

- 用于定义对象的**开发者友好字符串表示**（主要用于调试和日志记录）。
- 通常返回一串能明确再现对象状态的字符串。

**示例：**
```python
def __repr__(self):
    return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"
```
调用效果：
```python
print(repr(s1))  
# 输出：Student(name=Alice, age=20, student_id=S12345)
```

---

### 4.3 `__eq__`

- 用于定义对象之间“相等”（==）运算的行为。
- 比较的是对象某些关键属性（而非内存地址）。

**示例：**
```python
def __eq__(self, other):
    if isinstance(other, Student):
        return self.student_id == other.student_id
    return False
```

**测试效果：**
```python
s1 = Student("Alice", 20, "S12345")
s2 = Student("Alice", 21, "S12345")
s3 = Student("Tom", 22, "S67890")

print(s1 == s2)  # True，因为student_id相同
print(s1 == s3)  # False
```

---

## 5. 继承（Inheritance）

- 子类可以继承父类的方法和属性。
- 通过`super().__init__()`调用父类构造器。

**示例：**

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 继承Person的属性
        self.student_id = student_id
```

---

## 6. 今日编写的完整类结构

```text
Person类
  ├── 属性: name, age
  ├── 方法: introduce()

Student类 (继承Person)
  ├── 新增属性: student_id
  ├── 重写introduce()
  ├── 新增 __str__, __repr__, __eq__

Teacher类 (继承Person)
  ├── 新增属性: teacher_id
  ├── 重写introduce()
```

---

## 7. 总结与思考

- 理解了Python面向对象编程（OOP）三大核心要素：封装、继承、多态。
- 学会了使用特殊方法改善对象的打印效果和比较逻辑。
- 体会到合理设计类结构的重要性（比如 `Person` 作为父类，`Student` 和 `Teacher` 继承扩展）。
- 通过实操加深了对 `super()`、`self`、初始化方法的理解。
- 初步掌握了在PyCharm中使用Git进行版本控制和提交。

---

# 📌 附录：项目文件结构示意

```text
python_advanced_project/
  ├── person.py
  ├── student.py
  ├── teacher.py
  ├── main.py
  └── day1_notes.md
```

---

# 📌 附录：Git操作记录（参考）

```bash
git init
git remote add origin https://github.com/yesccai/python-advanced.git
git add .
git commit -m "Day 1: 完成OOP基础类与特殊方法"
git push origin main
```

---

# ✅ 今日成果

- [x] 3个类文件编写完成
- [x] 特殊方法添加测试成功
- [x] Git提交至GitHub
- [x] 学习笔记整理完毕

---