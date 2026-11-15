from casting import generate_hexagram
from analysis import analyze_hexagram
from display import display_hexagram


# 功能：依次调用起卦、分析和展示模块，完成一次完整起卦
# 输入：无
# 输出：在屏幕上展示六爻卦象

def main():
    # 1. 随机生成完整六爻数据，返回列表
    hexagram = generate_hexagram()

    # 2. 分析卦象，返回包含卦名、所属宫、序位及世应的字典
    analysis = analyze_hexagram(hexagram)

    # 3. 显示卦象，该函数直接打印内容，不返回分析数据
    display_hexagram(hexagram, analysis)


# 仅在直接运行 main.py 时启动程序
if __name__ == "__main__":
    main()
