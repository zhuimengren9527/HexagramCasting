
# 功能：显示卦象基本信息，并从上到下绘制六爻及动爻标记
# 输入：
#   hexagram：包含六个爻字典的列表
#   analysis：analyze_hexagram() 返回的分析结果字典
# 处理：先显示基本信息，再根据阴阳和动静绘制六爻
# 输出：通过 print() 打印卦象，不返回数据

def display_hexagram(hexagram, analysis):

    # 1. 显示基本信息
    # analysis：包含 name、palace、position、shi、ying 的字典
    print("卦名：", analysis["name"])
    print("所属宫：", analysis["palace"])
    print("八宫序位：", analysis["position"])

    # 2. 绘制六爻
    # hexagram 按初爻到上爻存储
    # reversed() 将展示顺序改为上爻到初爻
    
    # 2. 从上爻到初爻，依次绘制六爻
    for index, yao in enumerate(reversed(hexagram)):

        # 计算当前爻位
        yao_position = 6 - index

        # 判断世应标记
        mark = ""

        if yao_position == analysis["shi"]:
            mark = "世"
        elif yao_position == analysis["ying"]:
            mark = "应"

        # 根据阴阳属性生成爻的图形
        if yao["yin_yang"] == "阳":
            yao_symbol = "━" * 6
        else:
            yao_symbol = "━" * 2 + "  " + "━" * 2

        # 根据爻名判断动爻标记
        moving_mark = ""

        if yao["name"] == "老阳":
            moving_mark = "○"
        elif yao["name"] == "老阴":
            moving_mark = "×"

        # 统一输出爻形、动爻和世应标记
        print(f"{yao_symbol}  {moving_mark:<2} {mark}")


# 仅在直接运行 display.py 时执行测试
if __name__ == "__main__":

    # 测试时才需要从其他模块导入函数
    from casting import identify_number
    from analysis import analyze_hexagram

    # 构造包含动爻的火雷噬嗑
    test_hexagram = [
        identify_number(7),
        identify_number(6),
        identify_number(8),
        identify_number(7),
        identify_number(8),
        identify_number(9)
    ]

    # 获取分析结果
    analysis = analyze_hexagram(test_hexagram)

    # 展示卦象
    display_hexagram(test_hexagram, analysis)
