# HexagramCasting

一个基于 Python 开发的六爻起卦与京房八宫学习工具。

## 项目简介

HexagramCasting 是我在学习 Python 编程和中国传统文化过程中开发的个人学习项目。

程序通过随机生成六爻卦象，帮助使用者练习京房八宫的定宫方法、八宫序位以及世爻和应爻的位置判断。

项目以学习和练习为主要目的，采用**每回答一题立即反馈**的方式，帮助初学者及时纠正错误、熟悉八宫与世应规则。

## 主要功能

- 随机生成六爻卦象
- 显示阴阳爻及动爻标记
- 根据卦象识别六十四卦名称
- 练习八宫序位判断
- 练习所属宫判断
- 练习世爻、应爻的位置判断
- 每道题独立提交，即时反馈正确答案
- 支持重新起卦和滚动查看题目
- 已通过64卦核心定宫及世应算法的自动化测试

## Windows 软件下载安装

**当前发布版本：v0.1.0（Windows 图形界面版）**

[点击进入软件下载页面](https://github.com/zhuimengren9527/HexagramCasting/releases/tag/v0.1.0)

### 使用方法

1. 打开上方软件下载页面。
2. 在 **Assets** 中下载 `HexagramCasting.exe`。
3. 在 Windows 64 位电脑上双击运行。
4. 点击「起卦」，开始六爻八宫练习。
5. 按照提示依次回答八宫序位、所属宫、世爻和应爻位置。

**Windows EXE 版本无需单独安装 Python。**

注意：当前提供的是 Windows 电脑版本，不支持直接在 Android 或 iPhone 上运行。

## Python 源代码运行方法

如果希望通过 Python 运行源代码，需要安装 Python 3。

下载或克隆项目后，进入项目目录。

### 1. 启动图形界面

```bash
python app.py
```

### 2. 启动命令行练习

```bash
python practice.py
```

### 3. 随机生成并显示完整卦象分析

```bash
python main.py
```

### 4. 运行核心算法测试

```bash
python test_hexagrams.py
```

## 项目文件说明

| 文件 | 功能 |
|---|---|
| `config.py` | 八卦、六十四卦及八宫规则配置 |
| `casting.py` | 随机起卦与爻属性生成 |
| `analysis.py` | 卦象分析、定宫和世应判断 |
| `display.py` | 完整卦象的命令行显示 |
| `app.py` | Tkinter 图形界面程序 |
| `practice.py` | 命令行交互练习 |
| `main.py` | 随机起卦主程序 |
| `test_hexagrams.py` | 核心算法自动化测试 |

## 后续计划

根据实际使用需求，考虑提供网页版或进一步完善界面体验。

## 说明

本项目主要用于中国传统文化学习及 Python 编程实践。

欢迎对京房八宫、六爻学习或 Python 编程感兴趣的朋友交流。
