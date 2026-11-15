
# 功能：显示六爻练习题，不展示分析答案
# 输入：hexagram，包含六个爻属性字典的列表
# 处理：从上到下绘制阴阳爻，并显示动爻标记
# 输出：通过 print() 显示六爻图形
from casting import generate_hexagram
from analysis import analyze_hexagram

def display_question(hexagram):

    # 1. 从上爻到初爻遍历
    for yao in reversed(hexagram):

        # 2. 根据阴阳属性生成爻形
        if yao["yin_yang"] == "阳":
            yao_symbol = "━" * 6
        else:
            yao_symbol = "━" * 2 + "  " + "━" * 2

        # 3. 判断动爻标记
        # 每次循环都要重新初始化
        moving_mark = ""

        if yao["name"] == "老阳":
            moving_mark = "○"
        elif yao["name"] == "老阴":
            moving_mark = "×"

        # 4. 输出当前爻的图形与动爻标记
        # 注意：必须放在 for 循环内部
        print(f"{yao_symbol}  {moving_mark}")


# 功能：进行一次六爻定宫练习
# 输入：无，程序随机生成六爻
# 处理：显示卦象、接收答案、分析卦象、判断正误
# 输出：通过 print() 显示判断结果

def practice_palace():

    # 1. 随机生成六爻数据
    hexagram = generate_hexagram()

    # 2. 展示练习题，不提前显示答案
    display_question(hexagram)

    # 3. 接收用户输入
    answer_palace = input("请输入所属宫：").strip()

    # 4. 获取程序分析结果
    analysis = analyze_hexagram(hexagram)

    # 5. 提取正确的所属宫
    correct_palace = analysis["palace"]

    # 6. 判断用户答案
    if answer_palace == correct_palace:
        print("回答正确")
    else:
        print("回答错误")
        print("正确的所属宫是：", correct_palace)


# 只有直接运行 practice.py 时，才启动定宫练习
if __name__ == "__main__":
    practice_palace()


