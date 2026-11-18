
# 六爻交互练习模块
# 功能：随机生成六爻卦象，练习八宫序位、所属宫及世应位置的判断

from casting import generate_hexagram
from analysis import analyze_hexagram


# 功能：显示六爻练习题，不提前展示分析答案
# 输入：hexagram，包含六个爻属性字典的列表
# 处理：从上到下绘制阴阳爻，并显示动爻标记
# 输出：通过 print() 显示六爻图形

def display_question(hexagram):

    # 1. 从上爻到初爻遍历
    for yao in reversed(hexagram):

        # 2. 根据阴阳属性生成爻形
        if yao["yin_yang"] == "阳":
            yao_symbol = "━" * 6
        else:
            yao_symbol = "━" * 2 + "  " + "━" * 2

        # 3. 根据爻名判断动爻标记
        # 默认是静爻，不显示标记
        moving_mark = ""

        if yao["name"] == "老阳":
            moving_mark = "○"
        elif yao["name"] == "老阴":
            moving_mark = "×"

        # 4. 输出当前爻的图形和动爻标记
        print(f"{yao_symbol}  {moving_mark}")


# 功能：进行一次六爻综合练习
# 输入：无，程序自动随机生成一卦
# 处理：
#   1. 随机起卦并展示题目
#   2. 询问八宫序位并判断答案
#   3. 询问所属宫并判断答案
#   4. 询问世爻位置并判断答案
#   5. 询问应爻位置并判断答案
# 输出：通过 print() 显示答题结果
# 依赖：generate_hexagram()、analyze_hexagram()、display_question()

def practice_hexagram():

    # 1. 随机生成六爻数据
    # hexagram：包含六个爻属性字典的列表
    hexagram = generate_hexagram()

    # 2. 显示六爻图形，不提前显示答案
    display_question(hexagram)

    # 3. 计算标准答案
    # analysis：包含 name、position、palace、shi、ying
    # 这里只计算数据，不打印答案
    analysis = analyze_hexagram(hexagram)

    # 4. 第一题：判断八宫序位
    # answer_position：用户输入的序位，例如 "五世卦"
    # correct_position：程序计算的标准序位
    answer_position = input("请输入八宫序位：").strip()
    correct_position = analysis["position"]

    if answer_position == correct_position:
        print("八宫序位回答正确")
    else:
        print("八宫序位回答错误")
        print(f"正确的八宫序位是：{correct_position}")

    # 5. 第二题：判断所属宫
    # answer_palace：用户输入的宫名，例如 "巽"
    # correct_palace：程序计算的标准所属宫
    answer_palace = input("请输入所属宫：").strip()
    correct_palace = analysis["palace"]

    if answer_palace == correct_palace:
        print("所属宫回答正确")
    else:
        print("所属宫回答错误")
        print(f"正确的所属宫是：{correct_palace}")

    
    # 6. 第三题：判断世爻位置
    # answer_shi：用户输入的世爻位置，字符串，如 "5"
    # correct_shi：程序计算的标准世爻位置，整数，如 5

    answer_shi = input("请输入世爻位置（1-6）：").strip()

    correct_shi = analysis["shi"]

    # str()：将整数转换为字符串，便于与 input() 的结果比较
    if answer_shi == str(correct_shi):
        print("世爻位置回答正确")
    else:
        print("世爻位置回答错误")
        print(f"正确的世爻位置是：{correct_shi}")

    
    # 7. 第四题：判断应爻位置
    # answer_ying：用户输入的应爻位置，字符串，如 "2"
    # correct_ying：程序计算的应爻位置，整数，如 2

    answer_ying = input("请输入应爻位置（1-6）：").strip()

    correct_ying = analysis["ying"]

    # str()：将整数转换为字符串，与 input() 的结果进行比较
    if answer_ying == str(correct_ying):
        print("应爻位置回答正确")
    else:
        print("应爻位置回答错误")
        print(f"正确的应爻位置是：{correct_ying}")



# 只有直接运行 practice.py 时，才启动练习
if __name__ == "__main__":
    practice_hexagram()
    input("\n练习结束，按回车键退出...")
