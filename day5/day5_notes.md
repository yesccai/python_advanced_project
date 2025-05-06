以下是专为你定制的 `day5_notes.md` 模板笔记文件，涵盖今日主题“并发编程（线程与进程）”，结构清晰、适合项目归档或博客发布：

---

````markdown
# Day 5 学习笔记：Python 并发编程基础

---

## 🎯 今日目标

- 理解 Python 的并发模型：多线程与多进程
- 掌握 `threading` 和 `multiprocessing` 的基本用法
- 理解 GIL（全局解释器锁）对线程的影响
- 使用 `Queue` 实现线程/进程间通信
- 比较串行 / 多线程 / 多进程性能差异
- 实践典型 I/O 密集与 CPU 密集任务加速方案

---

## 🧵 一、多线程（threading）

### ✅ 创建线程

```python
import threading

def task():
    print("执行任务")

t = threading.Thread(target=task)
t.start()
t.join()
````

### ✅ 线程适用场景

* I/O 密集型任务（下载、网络、读写）
* GIL 不影响阻塞型操作的并发性能提升

---

## 🔁 二、多线程实战：模拟文件下载

```python
def download(file):
    print(f"开始下载 {file}")
    time.sleep(2)
    print(f"完成下载 {file}")
```

使用多个线程同时调用，实际运行时间缩短到 ≈ 单线程时间 / N。

---

## ⚙️ 三、多进程（multiprocessing）

### ✅ 创建进程

```python
from multiprocessing import Process

def calc():
    # CPU密集任务
    for i in range(10**7): pass

p = Process(target=calc)
p.start()
p.join()
```

### ✅ 适用场景

* CPU 密集型任务（计算、压缩、加密）
* 可绕过 GIL，真正实现多核并行

---

## 🧳 四、Queue 跨线程/进程通信

```python
import queue
q = queue.Queue()

q.put("数据")
data = q.get()
```

* `queue.Queue()`：适用于线程
* `multiprocessing.Queue()`：适用于进程

---

## 📈 五、性能对比结论

| 模式  | I/O 密集任务效果 | CPU 密集任务效果 | 是否受 GIL 限制  |
| --- | ---------- | ---------- | ----------- |
| 串行  | 最慢         | 最慢         | 否           |
| 多线程 | 明显加速       | 无明显提升      | 是（受 GIL 限制） |
| 多进程 | 提升有限（开销大）  | 明显加速       | 否           |

---

## 🧠 学习总结

* **GIL 并不阻碍 I/O 密集型线程并发**，阻碍的是 CPU 密集型并行
* 多线程适合轻任务 / 网络类脚本，开发更简单，线程共享内存
* 多进程适合高性能要求任务，支持多核，进程隔离但代价较高
* `Queue` 是线程/进程通信的可靠机制，避免资源竞争
* 实际项目中推荐使用 `concurrent.futures.ThreadPoolExecutor` 做线程池封装

---

## 📦 今日输出

* ✅ `thread_demo.py`：线程创建与 join
* ✅ `thread_download.py`：模拟并发下载
* ✅ `process_demo.py`：多进程任务测试
* ✅ `queue_thread.py` & `queue_process.py`：通信机制
* ✅ `performance_compare.py`：并发性能对比
* ✅ 本笔记文件：`day5_notes.md`

````

---

✅ 建议保存为：

```bash
day5/day5_notes.md
````

然后提交 Git：

```bash
git add day5/day5_notes.md
git commit -m "添加 Day 5 并发编程学习笔记"
git push
```