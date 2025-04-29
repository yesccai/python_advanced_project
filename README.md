```markdown
# python_advanced_project

> **Python高级编程学习项目**  
> 系统性练习面向对象编程（OOP）、设计模式、异常处理、日志记录与并发编程，夯实编程基本功。

---

## 📚 项目背景

本项目旨在通过实战演练，掌握 Python 高级编程特性，为后续数据工程、大数据开发、AI工程打下坚实基础。  
项目内容涵盖：  
- 面向对象编程（OOP）
- 常用设计模式（如工厂模式、单例模式）
- 异常与日志处理
- 多线程与多进程基础
- 数据处理与分析基础

所有代码均规范管理，配套学习笔记同步更新。

---

## 📅 学习计划

| 阶段 | 时间范围 | 学习内容 |
|:----|:--------|:--------|
| 第一阶段 | 2025年5月–6月 | Python高级用法、SQL进阶、Pandas数据处理、Linux基础、Git使用 |

---

## 📦 当前进度

### ✅ Day 1：类与对象基础

- 理解并掌握了 Python 类（Class）与对象（Instance）基础。
- 熟练应用了构造方法 `__init__` 初始化实例属性。
- 实现了常用特殊方法：
  - `__str__`：提升打印输出的可读性。
  - `__repr__`：增强调试友好性。
  - `__eq__`：自定义对象相等比较逻辑。
- 设计了合理的继承体系：
  - 父类：`Person`
  - 子类：`Student`、`Teacher`
- 使用 PyCharm 编写并调试代码。
- 完成了 Git 本地版本管理与 GitHub远程仓库同步。

---

### ✅ Day 2：继承、多态与图书馆系统实践

- 复习并实践了单继承、多继承、方法重写与多态机制。
- 通过“鸭子类型”实现对非继承对象的统一接口调用。
- 构建图书馆管理系统类结构，包含：
  - `Book`：图书类，含标题、作者、可借状态。
  - `Student` / `Teacher`：继承自 `Person`，实现不同借书策略。
  - `Library`：图书馆类，提供书籍管理功能。
- 编写两个测试脚本：
  - `main.py`：演示多态 + 鸭子类型调用 `speak()`。
  - `main_library.py`：模拟借书流程，输出如下：
    ```text
    小明 借了 《Python入门》
    《Python入门》 已被借出
    教师 李老师 借阅： 《算法导论》
    ```
- 总结继承、多态、鸭子类型的区别与使用场景，整理笔记 `day2_notes.md`。

---

## 📂 项目结构

```text
python_advanced_project/
├── day1/
│   ├── person.py
│   ├── student.py
│   ├── teacher.py
│   ├── main.py
│   └── day1_notes.md
├── day2/
│   ├── oop_inherit_poly.py
│   ├── main.py
│   ├── library_system.py
│   ├── main_library.py
│   └── day2_notes.md
└── README.md
```

---

## 🔧 使用说明

### 运行示例

```bash
cd python_advanced_project/day2
python main.py
python main_library.py
```

---

## 🧠 学习心得

- Python 的面向对象特性不仅支持传统继承，还因“鸭子类型”而极具灵活性。
- 多态和方法重写可以构建统一调用接口，提升系统扩展能力。
- 通过图书馆案例，实践了“面向接口编程”的设计思想。

---

## 🔗 后续计划

- ✅ Day 3：设计模式（简单工厂、抽象工厂）
- Day 4：异常处理、日志系统
- Day 5：并发编程
- 每阶段搭配项目实操，积累可展示作品集与博客输出内容。

---

## 📜 License

本仓库内容仅供个人学习与交流使用。禁止未经授权的转载或商用。

---

# ✨ 致未来的自己
保持日更，坚持积累，每一次Push，都是在为未来加码。🚀
```

---

✅ 更新方式：
将此内容覆盖你项目根目录的 `README.md` 文件，然后执行：

```bash
git add README.md
git commit -m "更新README：加入Day 2继承与图书馆系统内容"
git push
```

---