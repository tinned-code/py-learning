# ============================================
# 第二课：函数 和 类
# 跑法：python lesson2.py
# ============================================


# ---------- 第一段：函数 ----------

# def 是 define（定义）的缩写
# add 是给这个函数起的名字，你自己取，但最好说人话
# 括号里的 a 和 b 叫"参数"，意思是：这个函数需要你给它两块材料
def add(a, b):
    # return 是"把结果交还出去"，交还给调用它的人
    return a + b


# 现在调用它：给 2 和 3 两块材料，它就还给你 5
result = add(2, 3)
print(result)          # 屏幕上打 5

# 也可以不存下来，直接打印
print(add(10, 20))     # 屏幕上打 30


# 函数的好处：写一次，到处用
# 再来一个：给它一个名字，它还你一句问候
def greet(name):
    return "你好，" + name


print(greet("阿灯"))    # 屏幕上打 你好，阿灯
print(greet("小明"))    # 屏幕上打 你好，小明


# ---------- 第二段：类 ----------

# class 是"定义一个模板"
# Bird 就是模板的名字（习惯上首字母大写）
class Bird:
    # __init__ 是特殊名字，前后各两个下划线，念作"dunder init"
    # 每次你"造一只鸟"，Python 都会自动跑一遍这个方法
    def __init__(self, name, place):
        # self 就是"这一只鸟自己"，不能省
        # 等号右边的 name 是你传进来的材料，左边的 self.name 是存在这只鸟身上的
        self.name = name
        self.place = place

    # 这是鸟自己的一个本事，叫"方法"（其实就是写在类里面的函数）
    def introduce(self):
        # f"..." 叫 f-string，字符串前面加个 f，就能在花括号里塞变量
        print(f"我在{self.place}看到了{self.name}")
    def shout(self):
        print(f"{self.name}!!")

# 造一只具体的鸟。这一步叫"实例化"
# 注意：不用写 self，Python 自己会把这只鸟塞进 self
b1 = Bird("白鹡鸰", "校区湖边")
b2 = Bird("珠颈斑鸠", "老家院子")
b3 = Bird("夜鹭","河边栏杆")

# 让它说出自己的信息
b1.introduce()
b2.introduce()
b3.introduce()
b1.shout()

# ---------- 第三段：函数和类怎么配合 ----------

# 写一个函数，专门数一数有几只鸟
def count_birds(bird_list):
    # len() 是 Python 自带的函数，算"里面有几个"
    return len(bird_list)


all_birds = [b1, b2]        # 方括号里装一堆东西，这叫"列表"
print(count_birds(all_birds))    # 屏幕上打 2