---

```markdown
# Day 2 学习笔记：Python OOP高级特性（继承、多态、鸭子类型）

---

## 🧠 今日关键词

- 类继承（单继承、多继承）
- 方法重写（Override）
- 多态（Polymorphism）
- 鸭子类型（Duck Typing）
- 简单系统设计（图书馆借书系统）

---

## 🔁 继承（Inheritance）

### ✅ 概念

继承是指一个子类（Subclass）可以复用父类（Superclass）的属性和方法，并可以重写其行为。  
支持代码复用与功能扩展。

### ✅ 示例代码（单继承）：

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

## 👻 多态（Polymorphism）

### ✅ 定义

不同子类对象以统一方式调用同名方法时，自动执行各自的实现。  
即“一个接口，多种实现”。

### ✅ 示例：

```python
def make_it_speak(obj):
    print(obj.speak())

# Dog / Cat / Robot 都实现了 .speak()
```

- `make_it_speak()` 是一个典型的**多态应用函数**

---

## 🦆 鸭子类型（Duck Typing）

> “如果它像鸭子，会嘎嘎叫，那它就是鸭子。”

### ✅ 特点

Python是一门动态语言，不需要对象属于某个特定类，只要对象具有 `speak()` 方法就可以被接受为“鸭子”。

### ✅ 示例：

```python
class Robot:
    def speak(self):
        return "Beep boop"

make_it_speak(Robot())  # Beep boop
```

---

## 📘 图书馆系统设计练习

### ✅ 类结构

| 类名 | 作用 |
|------|------|
| `Book` | 表示一本图书 |
| `Person`（抽象） | 表示借书人父类 |
| `Student` / `Teacher` | 分别继承 Person，重写 `borrow_book()` 方法 |
| `Library` | 管理书籍的集合，提供 `add_book()` |

### ✅ 实现要点

- 使用继承复用 `Person` 基类行为
- 使用方法重写（`borrow_book()`）实现不同身份借书逻辑
- 使用状态标志 `book.available` 实现借阅状态控制

---

## ✅ 运行效果示例（main_library.py）

```text
小明 借了 《Python入门》
《Python入门》 已被借出
教师 李老师 借阅： 《算法导论》
```

---

## 🔧 今日收获

- 熟悉了 Python 的继承结构和方法重写机制
- 理解并实际应用了多态调用和鸭子类型思想
- 利用类封装完成了一个简易的图书馆管理系统
- 提交代码至 GitHub `day2/` 文件夹，完成第二天进度

---

## 📂 项目目录结构

```text
day2/
├── oop_inherit_poly.py       # Animal / Dog / Cat / Robot
├── main.py                   # 多态与鸭子类型测试
├── library_system.py         # 图书馆系统类结构
├── main_library.py           # 借书流程测试
└── day2_notes.md             # 今日笔记（本文件）
```

---

## 📌 Git 提交信息建议

```bash
git add day2/
git commit -m "Day 2: 完成继承、多态与图书馆系统类设计练习"
git push
```

---

> 下一步：Day 3 将学习 **设计模式**（简单工厂 + 抽象工厂），更进一步掌握“高内聚、低耦合”的程序结构思想。
```

---

✅ 这个笔记模板逻辑清晰、条理明确，可直接：
- 复制粘贴到 `day2_notes.md`
- 发布到 CSDN、知乎、GitHub仓库等
- 作为阶段性成果提交导师、面试展示材料

需要我为 Day 3（设计模式）提前安排内容模板吗？要的话我可以马上给你出一个 Day 3 专用计划💡！是否继续？