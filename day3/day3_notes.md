```markdown
# Day 3 学习笔记：设计模式实践（简单工厂 + 抽象工厂）

---

## 🎯 今日目标

- 理解什么是设计模式及其意义
- 掌握两种创建型设计模式：
  - 简单工厂模式（Simple Factory）
  - 抽象工厂模式（Abstract Factory）
- 运用继承与多态构建灵活的对象创建机制
- 通过代码实操理解工厂模式如何解耦业务与对象创建

---

## 🏭 简单工厂模式（Simple Factory）

### ✅ 定义  
通过一个工厂类根据参数决定返回哪个子类对象，客户端不直接调用具体类。

### ✅ 类图结构简述
```text
       Client
          |
     --------------
     |            |
 Factory -----> Product (抽象类/父类)
                  ↑
         ------------------
         |                |
     ConcreteA       ConcreteB
```

### ✅ 示例代码片段
```python
class AnimalFactory:
    @staticmethod
    def create_animal(kind):
        if kind == "dog":
            return Dog()
        elif kind == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
```

### ✅ 优缺点

| 优点 | 缺点 |
|------|------|
| 封装对象创建，客户端无需了解细节 | 增加新产品需修改工厂，违反开放-封闭原则 |
| 简化客户端代码 | 工厂类职责重，违背单一职责原则 |

---

## 🧩 抽象工厂模式（Abstract Factory）

### ✅ 定义  
提供一个创建**一组相关或相互依赖对象**的接口，无需指定它们具体的类。

### ✅ 类图结构简述

```text
     Client
        |
  -------------------
  |                 |
AbstractFactory   -> AbstractProductA / B
     ↑                     ↑
     |                     |
ConcreteFactoryA     ConcreteProductA1 / B1
ConcreteFactoryB     ConcreteProductA2 / B2
```

### ✅ 示例代码片段

```python
class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_textbox(self): return WinTextBox()
```

### ✅ 输出效果

```text
[Windows Button]
[Windows TextBox]
[Mac Button]
[Mac TextBox]
```

### ✅ 优缺点

| 优点 | 缺点 |
|------|------|
| 适用于“产品族”变化场景，扩展性强 | 新增单个产品类型需改所有工厂类，扩展粒度不够细 |
| 符合开闭原则 | 初学者理解难度较大 |

---

## ✅ 简单工厂 vs 抽象工厂 对比

| 维度 | 简单工厂 | 抽象工厂 |
|------|----------|----------|
| 产品数量 | 单一产品 | 多个相关产品（产品族） |
| 创建逻辑 | 工厂方法内部控制 | 工厂类接口提供多个产品方法 |
| 客户端依赖 | 仅依赖工厂 | 依赖抽象工厂接口 |

---

## 🧠 学习总结

- 工厂模式是典型的“解耦”手段，将对象创建过程从调用处抽离，便于维护。
- 简单工厂适合轻量级需求（如条件判断创建对象），但扩展性有限。
- 抽象工厂适用于跨平台、组件配套等场景，强调产品族整体一致性。
- 两者都体现了**面向接口编程**与**开放-封闭原则**的思想。

---

## 📦 今日输出

- ✅ `simple_factory.py` + `main_simple.py`
- ✅ `abstract_factory.py` + `main_abstract.py`
- ✅ 本笔记文件 `day3_notes.md`
- ✅ Git 提交成功并同步至 GitHub

---

## 📌 下一步预告：Day 4 —— 异常处理与日志系统
- 自定义异常类设计
- 多层嵌套异常捕获
- logging 模块的配置与封装实战
```

---