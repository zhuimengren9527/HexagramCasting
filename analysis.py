
# 卦象分析模块
# 功能：识别六十四卦名称、八宫序位、所属宫及世应位置
# 依赖：config.py 中预先定义的基础映射字典

from config import (
    trigrams,
    hexagram_names,
    palace_positions,
    shi_positions
)

def identify_trigrams(hexagram):
    
    lower_trigram = hexagram[0:3]
    upper_trigram = hexagram[3:6]
    lower_lines = []
    upper_lines = []
    for item in lower_trigram:
        lower_lines.append(item['yin_yang'])
    for item in upper_trigram:
        upper_lines.append(item["yin_yang"])
    lower_name = trigrams[tuple(lower_lines)]
    upper_name = trigrams[tuple(upper_lines)]

    return {
        "lower":lower_name,
        "upper":upper_name
    }

def identify_hexagram_name(trigram_info):

    upper_name = trigram_info["upper"]

    lower_name = trigram_info['lower']

    trigram_tuple = (upper_name,lower_name)

    hexagram_name = hexagram_names[trigram_tuple]
    
    # 返回六十四卦名称
    return hexagram_name

# 功能：比较上下卦对应爻位的阴阳是否相同，为判断八宫序位提供依据
# 输入：hexagram，包含六个爻信息字典的列表（初爻至上爻）
# 处理：分别提取上下卦，按底、中、顶的顺序逐爻比较阴阳
# 输出：comparison，包含三个"同"或"异"的列表
# 示例：["同", "同", "异"]，对应五世卦
def compare_trigrams(hexagram):
    lower_trigram = hexagram[0:3]
    upper_trigram = hexagram[3:6]

    comparison = []

    for i in range(3):
        lower_yao = lower_trigram[i]['yin_yang'] 
        upper_yao = upper_trigram[i]['yin_yang']

        if lower_yao == upper_yao:
            comparison.append('同')
        else:
            comparison.append('异')

    return comparison


# 功能：根据上下卦的阴阳同异关系，判断八宫序位
# 输入：comparison，包含三个"同"或"异"的列表（底、中、顶）
# 处理：将列表转换为元组，通过 palace_positions 字典查询序位
# 输出：position，字符串，如"本宫卦"、"五世卦"、"游魂卦"等
# 依赖：基础配置中的 palace_positions 字典
def identify_position(comparison):
    position = palace_positions[tuple(comparison)]
    return position


# 功能：将三爻卦的阴阳属性逐个反转
# 输入：lines，包含三个阴阳字符串的列表
#       例如 ["阳", "阴", "阴"]
# 处理：阳变阴，阴变阳，生成一个新的列表
# 输出：inverted_lines，例如 ["阴", "阳", "阳"]
# 依赖：无，不需要导入 config.py 中的字典

def invert_trigram_lines(lines):
    inverted_lines = []

    for line in lines:
        if line == "阳":
            inverted_lines.append("阴")
        else:
            inverted_lines.append("阳")

    return inverted_lines


# 功能：根据八宫序位，判断卦象所属八宫
# 输入：
#   trigram_info：上下卦名称字典，例如 {"lower": "震", "upper": "离"}
#   position：八宫序位，例如 "五世卦"
#   lower_lines：下卦阴阳列表，例如 ["阳", "阴", "阴"]
# 处理：
#   本宫至三世：直接取上卦
#   四世、五世、游魂：反转下卦，再查询 trigrams 字典
#   归魂：直接取下卦
# 输出：所属宫名称，例如 "巽"
# 依赖：
#   invert_trigram_lines()：本文件中已定义的阴阳反转函数
#   trigrams：从 config.py 导入的八卦映射字典

def identify_palace(trigram_info, position, lower_lines):

    if position in ("本宫卦", "一世卦", "二世卦", "三世卦"):
        return trigram_info["upper"]

    elif position in ("四世卦", "五世卦", "游魂卦"):
        inverted_lines = invert_trigram_lines(lower_lines)
        return trigrams[tuple(inverted_lines)]

    elif position == "归魂卦":
        return trigram_info["lower"]


# 功能：根据八宫序位，确定世爻和应爻的位置
# 输入：position，八宫序位字符串，例如"五世卦"
# 处理：
#   1. 查询预先定义的 shi_positions 字典，获取世爻位置
#   2. 根据世应相隔三爻的规则，计算应爻位置
# 输出：字典，例如 {"shi": 5, "ying": 2}
# 依赖：config.py 中预先定义的 shi_positions 字典

def identify_shi_ying(position):

    # shi_positions：键为八宫序位，值为世爻位置
    # 例如 shi_positions["五世卦"] 返回 5
    shi = shi_positions[position]

    # 根据世爻位置计算应爻位置
    if shi > 3:
        ying = shi - 3
    else:
        ying = shi + 3

    return {
        "shi": shi,
        "ying": ying
    }


# 功能：调用各个分析函数，完成六爻卦象的综合分析
# 输入：hexagram，包含六个爻信息字典的列表
# 处理：识别上下卦、卦名、八宫序位、所属宫及世应位置
# 输出：包含 name、position、palace、shi、ying 的字典
# 依赖：分析模块中已定义的各个辅助函数

def analyze_hexagram(hexagram):

    # 1. 识别上下卦名称
    # hexagram 是包含六个字典的列表
    # 例如：六个爻数依次为 7、8、8、7、8、7
    # 其中每个字典都包含 number、name、yin_yang、moving
    # identify_trigrams() 返回一个字典
    # 例如：{"lower": "震", "upper": "离"}
    trigram_info = identify_trigrams(hexagram)

    # 2. 根据上下卦名称，查询六十四卦名称
    # 输入 trigram_info：{"lower": "震", "upper": "离"}
    # 函数使用 hexagram_names 映射字典进行查询
    # 返回字符串，例如："火雷噬嗑"
    hexagram_name = identify_hexagram_name(trigram_info)

    # 3. 比较上下卦对应爻位的阴阳同异
    # 输入 hexagram：六个爻字典组成的列表
    # 按底、中、顶的顺序比较上下卦
    # 返回列表，例如：["同", "同", "异"]
    comparison = compare_trigrams(hexagram)

    # 4. 根据同异关系判断八宫序位，再确定世应位置
    # comparison：["同", "同", "异"]
    # identify_position() 返回字符串，例如："五世卦"
    # 依赖基础配置中的 palace_positions 字典
    position = identify_position(comparison)

    # position："五世卦"
    # identify_shi_ying() 返回字典
    # 例如：{"shi": 5, "ying": 2}
    # 依赖基础配置中的 shi_positions 字典
    shi_ying = identify_shi_ying(position)

    # 5. 提取下卦的阴阳属性，为后续定宫做准备
    # 原因：四世卦、五世卦和游魂卦，需要反转下卦的三个爻来判断所属宫
    # 上下卦名称已经保存在 trigram_info 中，无需重复识别
    # hexagram[0:3]：取初爻、二爻、三爻，得到三个完整的爻字典
    lower_trigram = hexagram[0:3]

    # 从三个爻字典中分别提取 yin_yang
    # 例如：下卦震，对应 ["阳", "阴", "阴"]
    # 注意：这里只提取阴阳属性，不进行反转
    lower_lines = []

    for item in lower_trigram:
        lower_lines.append(item["yin_yang"])

    # 6. 根据八宫序位和上下卦信息，判断所属宫
    # 输入：
    # trigram_info：{"lower": "震", "upper": "离"}
    # position："五世卦"
    # lower_lines：["阳", "阴", "阴"]
    # identify_palace() 返回字符串，例如："巽"
    palace = identify_palace(trigram_info, position, lower_lines)

    # 7. 汇总并返回最终分析结果
    # name：六十四卦名称，例如 "火雷噬嗑"
    # position：八宫序位，例如 "五世卦"
    # palace：所属宫，例如 "巽"
    # shi：世爻位置，例如 5
    # ying：应爻位置，例如 2
    # 返回值的数据类型是 dict（字典）
    return {
        "name":hexagram_name,
        "position":position,
        "palace":palace,
        "shi": shi_ying["shi"],
        "ying": shi_ying["ying"]
    }

# 测试函数
if __name__ == "__main__":

    from casting import identify_number

    # 构造火雷噬嗑的六爻数据
    test_hexagram = [
        identify_number(7),
        identify_number(8),
        identify_number(8),
        identify_number(7),
        identify_number(8),
        identify_number(7)
    ]

    # 测试上下卦识别
    trigram_info = identify_trigrams(test_hexagram)

    # 测试六十四卦名称识别
    hexagram_name = identify_hexagram_name(trigram_info)

    
    print("上下卦：", trigram_info)
    print("卦名：", hexagram_name)

    # 测试上下卦对应爻位的同异关系
    comparison = compare_trigrams(test_hexagram)
    
    print("阴阳同异：", comparison)

    # 测试八宫序位识别
    position = identify_position(comparison)

    print("八宫序位：", position)

    # 测试三爻阴阳反转
    lower_lines = ["阳", "阴", "阴"]

    inverted_lines = invert_trigram_lines(lower_lines)

    print("原始阴阳：", lower_lines)
    print("反转阴阳：", inverted_lines)

    
    # 测试所属宫判断
    # test_hexagram：之前构造的火雷噬嗑六爻数据
    # trigram_info：{"lower": "震", "upper": "离"}
    # position："五世卦"

    # 提取下卦三个爻的阴阳属性
    lower_trigram = test_hexagram[0:3]
    lower_lines = []

    for yao in lower_trigram:
        lower_lines.append(yao["yin_yang"])

    # 调用定宫函数
    palace = identify_palace(trigram_info, position, lower_lines)

    print("所属宫：", palace)

    # 测试世应位置
    shi_ying = identify_shi_ying(position)

    print("八宫序位：", position)
    print("世应位置：", shi_ying)

    # 综合测试：调用统一分析函数
    analysis_result = analyze_hexagram(test_hexagram)

    print("综合分析结果：", analysis_result)