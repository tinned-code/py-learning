#第三次复习

# ============================================
# 第三课：文件读写 + JSON
# 跑法：python lesson3.py
# ============================================

# 把 Python 自带的 json 工具箱拿过来
import json


# ---------- 第一步：造数据 ----------
# 花括号是字典，里面是"键: 值"的配对
bird1 = {"name": "白鹡鸰", "place": "校区湖边"}
bird2 = {"name": "珠颈斑鸠", "place": "老家院子"}
bird3 = {"name": "夜鹭", "place": "河边栏杆"}

# 方括号是列表，把三条记录装成一串
records = [bird1, bird2, bird3]


# ---------- 第二步：写进文件 ----------
# with = 用完自动关文件，不用手动 f.close()
# "w" = 写入模式（文件已存在会被整个清空重写！）
# encoding="utf-8" = 中文不乱码，Windows 上不能省
with open("birds.json", "w") as f:
    # json.dump(要存的东西, 存进哪个文件, 两个可选设置)
    # ensure_ascii=False = 中文原样存，不转成 \u767d 这种鬼东西
    # indent=2 = 每层缩进两格，人能看懂
    json.dump(records, f, ensure_ascii=False, indent=2)

print("写完了，去文件夹里看看 birds.json")


# ---------- 第三步：读回来 ----------
# "r" = 读取模式
with open("birds.json", "r") as f:
    # json.load 把文件里的文字还原成 Python 的列表和字典
    loaded = json.load(f)

print(loaded)

# 注意：读回来的是字典，不是 Bird 对象
# 所以用方括号取，不能用点
for b in loaded:
    print(f"{b['place']} 有 {b['name']}")

# 想再加一条？直接改列表，重新存一次就行
records.append({"name": "苍鹭", "place": "湿地"})
records.append({"name": "黄苇开鸟", "place": "荷花池塘"})
with open("birds.json", "w") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
    
print("又追加了2条，一共", len(records), "条")

with open("birds.json", "r") as f:
    # json.load 把文件里的文字还原成 Python 的列表和字典
    loaded = json.load(f)

print(loaded)

# 注意：读回来的是字典，不是 Bird 对象
# 所以用方括号取，不能用点
for b in loaded:
    print(f"{b['place']} 有 {b['name']}")
    
