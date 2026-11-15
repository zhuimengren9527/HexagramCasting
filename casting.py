import random

# 起三个数字相加得到6、7、8或者9（对应一爻）
def generate_yao_number():
    number = 0
    for i in range(3):
        coin = random.choice([2,3])
        number += coin
    return number


# 功能：根据爻数识别名称、阴阳属性和动静状态
# 输入：整数6、7、8、9
# 输出：包含爻属性的字典
def identify_number(number):
    if number == 6 :
        numeric_attribute = {
            "number": 6,
            "name": "老阴",
            "yin_yang": "阴",
            "moving": True
        }
    elif number == 7 :
        numeric_attribute = {
            "number": 7,
            "name": "少阳",
            "yin_yang": "阳",
            "moving": False
        }
    elif number == 8 :
        numeric_attribute = {
            "number":8,
            "name":"少阴",
            "yin_yang":"阴",
            "moving":False
        }
    elif number == 9 :
        numeric_attribute = {
            "number": 9,
            "name": "老阳",
            "yin_yang": "阳",
            "moving": True
        }
    else:
        raise ValueError("无效的爻数，只能是6、7、8、9")
    
    return numeric_attribute


# 重复六次，生成六爻列表
def generate_hexagram():
    hexagram = []
    for i in range(6):
        number = generate_yao_number()
        numeric_attribute = identify_number(number)
        hexagram.append(numeric_attribute)
    return hexagram


# 以下代码仅在直接运行 casting.py 时执行
# 当其他文件通过 import 导入 casting.py 时，不执行这里的测试

if __name__ == "__main__":

    # 调用起卦函数，生成六个爻
    test_hexagram = generate_hexagram()

    # 检查六爻数量
    print("六爻数量：", len(test_hexagram))

    # 显示每个爻的属性
    for yao in test_hexagram:
        print(yao)
