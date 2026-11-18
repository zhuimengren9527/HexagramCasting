
# 六爻图形界面程序
# 功能：点击起卦按钮，随机生成并显示六爻

import tkinter as tk

from casting import generate_hexagram
from analysis import analyze_hexagram

# 保存当前卦象的分析结果
# state：字典，用于让不同函数共享当前卦象信息
# "analysis"：字典的键
# None：尚未起卦，还没有分析结果
state = {
    "analysis": None
}

# 功能：响应起卦按钮
# 输入：无
# 输出：在窗口中更新六爻图形
def cast():
    hexagram = generate_hexagram()

    # 分析当前卦象，并将结果保存到 state 中
    state["analysis"] = analyze_hexagram(hexagram)
    lines = []

    for yao in reversed(hexagram):
        if yao["yin_yang"] == "阳":
            symbol = "━━━━━━"
        else:
            symbol = "━━  ━━"

        moving_mark = ""
        if yao["name"] == "老阳":
            moving_mark = "○"
        elif yao["name"] == "老阴":
            moving_mark = "×"

        lines.append(f"{symbol}  {moving_mark}")

    # 将六行文本更新到窗口标签中
    hexagram_label.config(text="\n".join(lines))

    # 清空上一卦的输入
    position_entry.delete(0, tk.END)
    palace_entry.delete(0, tk.END)

    # 清空上一卦的反馈
    feedback_label.config(text="")
    palace_feedback_label.config(text="")

    # 清空第三题的输入
    shi_entry.delete(0, tk.END)

    # 清空第三题的反馈
    shi_feedback_label.config(text="")

    # 清空第四题的输入框
    ying_entry.delete(0, tk.END)

    # 清空第四题的反馈标签
    ying_feedback_label.config(text="")

# 功能：判断用户输入的八宫序位
# 输入：从 position_entry 获取答案
# 处理：与当前卦象的正确序位比较
# 输出：通过 feedback_label 显示判断结果


def submit_position():

    # 1. 检查是否已经起卦
    if state["analysis"] is None:
        feedback_label.config(text="请先点击起卦按钮")
        return

    # 2. 获取用户输入的答案
    answer_position = position_entry.get().strip()

    # 3. 读取当前卦象的正确序位
    correct_position = state["analysis"]["position"]

    # 4. 判断正误并立即反馈
    if answer_position == correct_position:
        feedback_label.config(text="八宫序位回答正确")
    else:
        feedback_label.config(
            text=f"回答错误，正确答案是：{correct_position}"
        )

    

# 功能：判断用户输入的所属宫是否正确
# 输入：从 palace_entry 读取用户答案
# 处理：与当前卦象的正确所属宫进行比较
# 输出：通过 palace_feedback_label 显示判断结果

def submit_palace():

    # 1. 检查是否已经起卦
    if state["analysis"] is None:
        palace_feedback_label.config(text="请先点击起卦按钮")
        return

    # 2. 获取第二题的用户答案
    answer_palace = palace_entry.get().strip()

    # 3. 获取第二题的标准答案
    correct_palace = state["analysis"]["palace"]

    # 4. 判断答案是否正确
    # 请你在这里独立完成 if...else
    # 正确：显示“所属宫回答正确”
    # 错误：显示正确的所属宫
    if answer_palace == correct_palace:
        palace_feedback_label.config(text="所属宫回答正确")
    else:
        palace_feedback_label.config(
            text=f"回答错误，正确答案是：{correct_palace}"
        )

def submit_shi():

    # 1.检查是否已经起卦
    if state["analysis"] is None:
        shi_feedback_label.config(text="请先点击起卦按钮")
        return

    # 2.获取第三题的用户答案
    answer_shi = shi_entry.get().strip()

    # 3.获取第三题的标准答案
    correct_shi = state["analysis"]["shi"]

    # 4.判断答案是否正确
    if answer_shi == str(correct_shi):
        shi_feedback_label.config(text="世爻位置回答正确")
    else:
        shi_feedback_label.config(
            text=f"回答错误，正确答案是：{correct_shi}"
        )

def submit_ying():
    # 1.检查是否已经起卦
    if state["analysis"] is None:
        ying_feedback_label.config(text="请先点击起卦按钮")
        return

    # 2.获取第四题的用户答案
    answer_ying = ying_entry.get().strip()

    # 3.获取第三题的标准答案
    correct_ying = state["analysis"]["ying"]

    # 4.判断答案是否正确
    if answer_ying == str(correct_ying):
        ying_feedback_label.config(text="应爻位置回答正确")
    else:
        ying_feedback_label.config(
            text=f"回答错误，正确答案是:{correct_ying}"
        )

# 1. 创建主窗口
root = tk.Tk()
root.title("HexagramCasting - 六爻练习")
root.geometry("480x720")

# 2. 创建标题
title_label = tk.Label(
    root,
    text="六爻八宫练习",
    font=("Microsoft YaHei", 18)
)
title_label.pack(pady=20)

# 3. 创建起卦按钮
cast_button = tk.Button(
    root,
    text="起卦",
    font=("Microsoft YaHei", 14),
    command=cast
)
cast_button.pack(pady=10)

# 4. 创建显示卦象的区域
hexagram_label = tk.Label(
    root,
    text="请点击起卦按钮",
    font=("Consolas", 20),
    justify="left"
)
hexagram_label.pack(pady=20)


# 创建可滚动的练习区域
questions_area = tk.Frame(root)
questions_area.pack(fill="both", expand=True)

# 创建画布，用来显示练习题
questions_canvas = tk.Canvas(
    questions_area,
    highlightthickness=0
)

# 创建垂直滚动条
questions_scrollbar = tk.Scrollbar(
    questions_area,
    orient="vertical",
    command=questions_canvas.yview
)

# 让滚动条与画布关联
questions_canvas.config(
    yscrollcommand=questions_scrollbar.set
)

questions_scrollbar.pack(side="right", fill="y")
questions_canvas.pack(side="left", fill="both", expand=True)

# 创建容器，后面的练习题全部放入这里
questions_frame = tk.Frame(questions_canvas)

frame_id = questions_canvas.create_window(
    (0, 0),
    window=questions_frame,
    anchor="nw"
)

# 内容高度变化时，更新可滚动范围
questions_frame.bind(
    "<Configure>",
    lambda event: questions_canvas.config(
        scrollregion=questions_canvas.bbox("all")
    )
)

# 让练习题容器的宽度与画布一致
questions_canvas.bind(
    "<Configure>",
    lambda event: questions_canvas.itemconfig(
        frame_id, width=event.width
    )
)

# 在 Windows 上使用鼠标滚轮滚动练习题
questions_canvas.bind_all(
    "<MouseWheel>",
    lambda event: questions_canvas.yview_scroll(
        -int(event.delta / 120), "units"
    )
)

# 5. 创建八宫序位练习区域

# 创建题目提示标签
position_label = tk.Label(
    questions_frame,
    text="第一题：请输入八宫序位",
    font=("Microsoft YaHei", 12)
)
position_label.pack(pady=5)

# 创建用户答案输入框
position_entry = tk.Entry(
    questions_frame,
    font=("Microsoft YaHei", 12),
    width=16
)
position_entry.pack(pady=5)


# 创建提交八宫序位答案的按钮
submit_button = tk.Button(
    questions_frame,
    text="提交答案",
    font=("Microsoft YaHei", 12),
    command=submit_position
)

submit_button.pack(pady=10)

# 创建答案反馈标签
# 初始文字为空，等待用户提交答案后更新
feedback_label = tk.Label(
    questions_frame,
    text="",
    font=("Microsoft YaHei", 12)
)

# 将反馈标签放到窗口中
feedback_label.pack(pady=5)


# 6. 第二题：所属宫练习

# 创建第二题的提示标签
palace_label = tk.Label(
    questions_frame,
    text="第二题：请输入所属宫",
    font=("Microsoft YaHei", 12)
)
palace_label.pack(pady=5)

# 创建所属宫输入框
palace_entry = tk.Entry(
    questions_frame,
    font=("Microsoft YaHei", 12),
    width=16
)
palace_entry.pack(pady=5)

# 第二题：提交按钮
palace_submit_button = tk.Button(
    questions_frame,
    text="提交所属宫答案",
    font=("Microsoft YaHei", 12),
    command=submit_palace
)
palace_submit_button.pack(pady=10)

# 第二题：反馈标签
palace_feedback_label = tk.Label(
    questions_frame,
    text="",
    font=("Microsoft YaHei", 12)
)
palace_feedback_label.pack(pady=5)

# 7.第三题：世爻位置练习

# 创建第三题的提示标签
shi_label = tk.Label(
    questions_frame,
    text="第三题：请输入世爻位置",
    font=("Microsoft YaHei",12)
)
shi_label.pack(pady=5)

# 创建世位置输入框
shi_entry = tk.Entry(
    questions_frame,
    font=("Microsoft YaHei",12),
    width=16
)
shi_entry.pack(pady=5)

# 第三题：提交按钮
shi_submit_button = tk.Button(
    questions_frame,
    text="提交世爻位置答案",
    font=("Microsoft YaHei",12),
    command=submit_shi
)
shi_submit_button.pack(pady=10)

# 第三题：反馈标签
shi_feedback_label = tk.Label(
    questions_frame,
    text="",
    font=("Microsoft YaHei",12)
)
shi_feedback_label.pack(pady=5)

# 8.第四题：应爻位置练习

# 创建第四题的提示标签
ying_label = tk.Label(
    questions_frame,
    text="第四题：请输入应爻位置",
    font=("Microsoft YaHei",12)
)
ying_label.pack(pady=5)

# 创建应爻位置输入框
ying_entry = tk.Entry(
    questions_frame,
    font=("Microsoft YaHei",12),
    width=16
)
ying_entry.pack(pady=5)

# 第四题：提交按钮
ying_submit_button = tk.Button(
    questions_frame,
    text="提交应爻位置答案",
    font=("Microsoft YaHei",12),
    command=submit_ying
)
ying_submit_button.pack(pady=10)

# 第四题：反馈标签
ying_feedback_label = tk.Label(
    questions_frame,
    text="",
    font=("Microsoft YaHei",12)
)
ying_feedback_label.pack(pady=5)
# 9. 启动图形界面
root.mainloop()
