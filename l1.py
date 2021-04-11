from pywinauto import application,Application
app=application.Application()
# app.start('notepad.exe')
# app.connect(path="C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
# app.window(class_name="微信文件").print_control_identifiers(depth = None, filename = None)
# app.top_window().print_control_identifiers()
# Untitled_notepad = u'无标题 – 记事本'
# app.top_window()['Edit'].draw_outline()

# app.connect(path='notepad.exe')
# app.top_window().draw_outline()
import time

app = Application().start("notepad.exe")

# 窗体选择
title_notepad = u"无标题-记事本"
# app[title_notepad]
# 选择一个菜单项
app[title_notepad].menu_select("帮助->关于记事本")

time.sleep(2)

# 点击新弹出窗体的 确定按钮
out_note = u"关于记事本"
button_name_ok = u"确定"
app[out_note][button_name_ok].click()

# 查看一个窗体都有哪些控件，子窗体，菜单
# print(app[title_notepad].print_control_identifiers())

# 输入一些文字
app[title_notepad].Edit.type_keys("Pywinauto works!\n", with_spaces=True, with_newlines=True)
app[title_notepad].Edit.type_keys("hello world!\n", with_spaces=True, with_newlines=True)

# 选择编辑菜单的
app[title_notepad].menu_select("编辑->时间/日期")

app[title_notepad].maximize()  # 窗口最大化
app[title_notepad].minimize()  # 窗口最小化