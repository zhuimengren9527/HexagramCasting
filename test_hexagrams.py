
# 六爻系统自动化测试模块
# 功能：生成64种阴阳组合，验证卦名、所属宫、八宫序位及世应位置

# product()：生成所有可能的有序组合
from itertools import product

# 从起卦模块导入数字识别函数
from casting import identify_number

# 从分析模块导入综合分析函数
from analysis import analyze_hexagram

# 八宫序位顺序
position_order = [
    "本宫卦", "一世卦", "二世卦", "三世卦",
    "四世卦", "五世卦", "游魂卦", "归魂卦"
]

# 京房八宫标准答案
standard_palaces = {
    "乾": [
        "乾为天", "天风姤", "天山遁", "天地否",
        "风地观", "山地剥", "火地晋", "火天大有"
    ],
    "兑": [
        "兑为泽", "泽水困", "泽地萃", "泽山咸",
        "水山蹇", "地山谦", "雷山小过", "雷泽归妹"
    ],
    "离": [
        "离为火", "火山旅", "火风鼎", "火水未济",
        "山水蒙", "风水涣", "天水讼", "天火同人"
    ],
    "震": [
        "震为雷", "雷地豫", "雷水解", "雷风恒",
        "地风升", "水风井", "泽风大过", "泽雷随"
    ],
    "巽": [
        "巽为风", "风天小畜", "风火家人", "风雷益",
        "天雷无妄", "火雷噬嗑", "山雷颐", "山风蛊"
    ],
    "坎": [
        "坎为水", "水泽节", "水雷屯", "水火既济",
        "泽火革", "雷火丰", "地火明夷", "地水师"
    ],
    "艮": [
        "艮为山", "山火贲", "山天大畜", "山泽损",
        "火泽睽", "天泽履", "风泽中孚", "风山渐"
    ],
    "坤": [
        "坤为地", "地雷复", "地泽临", "地天泰",
        "雷天大壮", "泽天夬", "水天需", "水地比"
    ]
}

expected_shi_ying = {
    "本宫卦": (6, 3),
    "一世卦": (1, 4),
    "二世卦": (2, 5),
    "三世卦": (3, 6),
    "四世卦": (4, 1),
    "五世卦": (5, 2),
    "游魂卦": (4, 1),
    "归魂卦": (3, 6)
}


# 仅在直接运行测试文件时执行
if __name__ == "__main__":

    # 检查八宫标准答案是否完整
    assert len(standard_palaces) == 8
    assert all(len(names) == 8 for names in standard_palaces.values())

    # 检查八宫序位数量
    assert len(position_order) == 8

    # 检查世应标准答案数量
    assert len(expected_shi_ying) == 8

    print("基础测试数据检查通过")

    
    # 1. 生成64种阴阳组合
    # 7为少阳，8为少阴，每组包含六个爻
    combinations = list(product([7, 8], repeat=6))

    # 2. 创建列表，保存全部64卦的分析结果
    results = []

    # 3. 外层循环：每次处理一组六爻数字
    for numbers in combinations:

        # 每一卦都要重新创建空列表
        test_hexagram = []

        # 内层循环：将六个数字转换为爻字典
        for number in numbers:
            yao_info = identify_number(number)
            test_hexagram.append(yao_info)

        # 分析当前卦象
        analysis = analyze_hexagram(test_hexagram)

        # 保存当前卦的分析结果
        results.append(analysis)

    # 4. 验证结果数量和卦名唯一性
    assert len(results) == 64
    assert len({result["name"] for result in results}) == 64

    print("64卦生成与分析测试通过")
    print("分析结果数量：", len(results))

    
    # 5. 将京房八宫标准序列转换为查询字典
    # standard_palaces：宫名对应八个卦名的字典
    # position_order：八种序位的固定顺序
    # standard_answers：卦名对应(所属宫, 八宫序位)
    #
    # 例如：
    # standard_answers["火雷噬嗑"] = ("巽", "五世卦")

    standard_answers = {}

    for palace, names in standard_palaces.items():

        for index, name in enumerate(names):

            standard_answers[name] = (
                palace,
                position_order[index]
            )

    # 验证标准答案数量
    assert len(standard_answers) == 64

    print("标准答案查询字典建立成功")

    
    # 6. 逐卦比较程序计算结果与标准答案
    # results：程序生成的64卦分析结果
    # standard_answers：预先建立的64卦标准答案字典
    # passed：保存测试通过的卦名
    # failed：保存测试失败的详细信息

    passed = []
    failed = []

    for result in results:

        # 1. 提取当前卦名
        # 例如："火雷噬嗑"
        name = result["name"]

        # 2. 获取程序实际计算结果
        # 例如：("巽", "五世卦")
        actual = (result["palace"], result["position"])

        # 3. 根据卦名查询标准答案
        # get()：如果没有找到卦名，则返回 None
        expected = standard_answers.get(name)

        # 4. 比较 actual 和 expected
        
        # 4. 比较程序计算结果与标准答案
        if actual == expected:

            # 如果一致，将当前卦名加入通过列表
            passed.append(name)

        else:

            # 如果不一致，保存卦名、实际结果和标准答案
            failed.append({
                "name": name,
                "actual": actual,
                "expected": expected
            })


    # 5. 输出测试统计
    print("测试总数：", len(results))
    print("通过数量：", len(passed))
    print("失败数量：", len(failed))
    print("失败详情：", failed)
    
    # 确保64卦全部参与验证
    assert len(passed) + len(failed) == len(results)

    # 确保64卦的所属宫和八宫序位全部正确
    assert len(failed) == 0


    # 7. 验证64卦的世应位置
    # results：程序生成的64卦分析结果
    # expected_shi_ying：预先建立的世应标准答案字典
    # shi_ying_passed：保存通过测试的卦名
    # shi_ying_failed：保存失败测试的详细信息

    shi_ying_passed = []
    shi_ying_failed = []

    for result in results:

        # 1. 提取当前卦名
        name = result["name"]

        # 2. 获取程序计算的世应位置
        # actual：元组，例如 (5, 2)
        actual = (result['shi'],result['ying'])

        # 3. 根据当前八宫序位查询标准世应位置
        # expected：元组，例如 (5, 2)
        expected = expected_shi_ying[result["position"]]

        # 4. 比较实际结果与标准答案
        # 如果相同，保存到 shi_ying_passed
        # 如果不同，保存到 shi_ying_failed
        if actual == expected:
            shi_ying_passed.append(name)
        else:
            shi_ying_failed.append(
                {
                    "name": name,
                    "actual": actual,
                    "expected": expected
                }
            )

    # 5. 输出测试统计
    print("测试总数：", len(results))
    print("通过数量：", len(shi_ying_passed))
    print("失败数量：", len(shi_ying_failed))
    print("失败详情：", shi_ying_failed)

    # 检查64卦是否全部参与测试，没有遗漏
    assert len(shi_ying_passed) + len(shi_ying_failed) == len(results)

    # 检查所有世应位置是否都符合标准答案
    assert len(shi_ying_failed) == 0

    # 所有测试均通过后，才执行以下语句
    print("\n全部64卦核心算法测试通过！")