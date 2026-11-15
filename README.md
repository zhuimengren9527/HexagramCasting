# HexagramCasting

一个基于 Python 开发的六爻起卦与京房八宫学习工具。

## 项目简介

HexagramCasting 是我在学习 Python 编程和中国传统文化过程中开发的个人学习项目。

程序通过随机生成六爻卦象，帮助使用者练习京房八宫的定宫方法、八宫序位以及世爻和应爻的位置判断。

项目以学习和练习为主要目的，采用每回答一题立即反馈的方式，方便初学者及时纠正错误。

## 主要功能

- 随机生成六爻卦象
- 显示阴阳爻及动爻标记
- 识别六十四卦名称
- 判断八宫序位
- 判断所属宫
- 判断世爻、应爻的位置
- 交互式答题，并即时显示判断结果
- 对64卦核心定宫及世应算法进行自动化验证

## 使用方法

**运行环境：** Python 3

当前版本采用命令行交互方式，需要先安装 Python。

下载项目源代码后，进入项目目录。

启动六爻练习：

`python practice.py`

随机生成并显示完整卦象分析：

`python main.py`

运行核心算法测试：

`python test_hexagrams.py`

## 项目文件说明

- `config.py`：八卦、六十四卦及八宫规则配置
- `casting.py`：随机起卦与爻属性生成
- `analysis.py`：卦象分析、定宫和世应判断
- `display.py`：完整卦象的终端显示
- `practice.py`：交互式练习程序
- `main.py`：随机起卦主程序
- `test_hexagrams.py`：核心算法自动化测试

## 后续计划

- 提供无需安装 Python 的 Windows 可执行版本
- 根据实际使用需求，考虑提供网页版

## 说明

本项目主要用于传统文化学习及 Python 编程实践。

欢迎对京房八宫、六爻学习或 Python 编程感兴趣的朋友交流。# HexagramCasting
A Python tool for I Ching hexagram casting and practice
