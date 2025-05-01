---

```markdown
# Day 4 学习笔记：异常处理与日志系统

---

## 🎯 今日目标

- 掌握 Python 异常处理结构（try / except / else / finally）
- 能够编写自定义异常类用于精确控制程序行为
- 熟悉 `logging` 模块的基本用法与配置方法
- 封装一个通用日志类，用于后续所有项目的日志输出

---

## 🧨 一、异常处理基础语法

### ✅ 常用结构：

```python
try:
    # 可能出错的代码块
except ExceptionType as e:
    # 异常处理逻辑
else:
    # 无异常时执行
finally:
    # 无论如何都会执行
```

### ✅ 示例代码：

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "不能除以 0"
    except TypeError as e:
        return f"类型错误: {e}"
    finally:
        print("结束一次除法操作")
```

---

## ⚙️ 二、自定义异常类

通过继承内置 `Exception` 类，创建具有业务含义的异常。

```python
class InvalidUsernameError(Exception):
    def __init__(self, username):
        super().__init__(f"无效用户名: {username}")
```

调用：

```python
def check_username(name):
    if len(name) < 3:
        raise InvalidUsernameError(name)
```

✅ 好处：增强语义表达 + 可读性 + 精准控制流程

---

## 🧾 三、日志系统 logging 模块

### ✅ 常见日志级别：

| 级别 | 函数 | 说明 |
|------|------|------|
| DEBUG | `logger.debug()` | 调试信息 |
| INFO | `logger.info()` | 程序运行状态 |
| WARNING | `logger.warning()` | 警告（但不会中断） |
| ERROR | `logger.error()` | 错误事件 |
| CRITICAL | `logger.critical()` | 严重错误，程序可能终止 |

---

### ✅ logging 基础配置

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

- `filename`: 输出日志到文件
- `level`: 最低记录级别（INFO以上）
- `format`: 日志格式（时间 + 等级 + 内容）

---

## 🧱 四、封装通用日志类

封装一个带文件输出和控制台输出的日志工具类 `Log`：

```python
class Log:
    def __init__(self, name='app', log_file='runtime.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler(log_file, encoding='utf-8')
        sh = logging.StreamHandler()

        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(fmt)
        sh.setFormatter(fmt)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def info(self, msg): self.logger.info(msg)
    def error(self, msg): self.logger.error(msg)
    def warn(self, msg): self.logger.warning(msg)
```

调用示例：

```python
log = Log()
log.info("程序启动")
log.warn("警告信息")
log.error("错误发生")
```

---

## 📌 日志输出效果（UTF-8 编码）

```text
2025-05-01 22:00:00,123 - INFO - 程序启动
2025-05-01 22:00:01,456 - WARNING - 注意事项
2025-05-01 22:00:02,789 - ERROR - 错误日志写入成功
```

✅ 同时写入 `runtime.log` 文件 + 控制台输出，便于调试与保存

---

## 🧠 学习总结

- Python 异常处理结构清晰，能细粒度捕捉并恢复程序运行
- 自定义异常可表达更强的业务含义，避免泛用 `ValueError`
- `logging` 是生产级日志记录标准，比 `print()` 更专业可控
- 日志封装后可复用于任何工程项目，提升工程化水平
- 文件输出需明确指定 `encoding='utf-8'`，避免跨平台乱码

---

## 📦 今日输出

- ✅ `try_except_demo.py`：异常结构演练
- ✅ `custom_exception.py`：自定义异常使用
- ✅ `logger_basic.py`：基础日志测试
- ✅ `logger_configured.py`：配置格式与文件输出
- ✅ `logger_wrapper.py`：封装通用日志类
- ✅ `main.py`：测试输出与日志合并
- ✅ 本笔记文件 `day4_notes.md`
```

---