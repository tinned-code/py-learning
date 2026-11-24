# py-learning

Python 与 Git 从零入门的练习仓库。

从"不知道代码该写在哪"，一路学到能建仓库、开分支、推 GitHub。

## 环境

- Python 3.12
- Git 2.x
- Windows（PowerShell）

## 目录里有什么

| 文件 | 内容 |
|---|---|
| `first.py` | 第一个 Python 程序，只有一行 `print` |
| `lesson2.py` | 函数与类：`def`、`return`、`class`、`__init__`、`self` |
| `lesson3.py` | 文件读写与 JSON：`open`、`json.dump`、`json.load` |
| `lesson4.py` | 虚拟环境与 pip：用 `colorama` 输出彩色文字 |
| `birds.json` | lesson3 跑出来的数据 |
| `birds_utf8.json` | 编码对照用，同一份内容存成 UTF-8 |

## 怎么跑起来

### 1. 克隆下来

```bash
git clone https://github.com/tinned-code/py-learning.git
cd py-learning
```

### 2. 建虚拟环境

```bash
python -m venv .venv
```

### 3. 打开虚拟环境

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

如果被系统的执行策略拦住，用这条等价的命令，效果一样：

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
```

### 4. 装依赖

```bash
python -m pip install colorama
```

### 5. 跑

```bash
python lesson2.py
python lesson3.py
python lesson4.py
```

`lesson4.py` 需要第 4 步装好的 `colorama`，另外两个只用标准库。

## 关于编码

仓库里所有文件都是 **UTF-8**。

Windows 上有个坑：`open()` 不写 `encoding="utf-8"` 时，默认用系统编码（GBK）。程序自己读自己写不会报错，但文件已经不是 UTF-8 了，换一个程序打开就是乱码。

所以读写文件一律显式写：

```python
with open("birds.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## 记下来的几个坑

- **全角符号**：中文输入法打出的 `（）`、`""`、`，` 在 Python 里是非法字符，报 `SyntaxError: invalid character`。写代码前切英文输入法。
- **双击 `.py` 不是运行**：在 Windows 上双击只会用编辑器打开它。运行要敲 `python 文件名.py`。
- **`python -m pip` 而不是 `pip`**：机器上装了多个 Python 时，裸 `pip` 可能装到另一个解释器里去。
- **`.venv` 不进仓库**：本机环境别提交，别人自己 `python -m venv` 重建。
- **分支是平行世界**：切到别的分支，工作区里的文件真的会变；切回来又变回去。

## License

MIT