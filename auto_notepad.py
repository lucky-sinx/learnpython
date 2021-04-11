from pywinauto import application,Application
import time
import subprocess,uiautomation
import os
# app=Application().start('notepad.exe')
#
# title_notepad = u"无标题-记事本"
# app[title_notepad].SetTopmost(True)
# 点击新弹出窗体的 确定按钮
# out_note = u"关于记事本"
# button_name_ok = u"确定"
# app[out_note][button_name_ok].draw_outline(colour='red')
# time.sleep(2)
# app[out_note][button_name_ok].click()

# 点击页面设置的确定按钮
# new_title=u'页面设置'
# button_name=u'确定'
#
# app[new_title][button_name].draw_outline()
# time.sleep(1)
# app[new_title].print_control_identifiers()
subprocess.Popen('notepad.exe')
notepad=uiautomation.WindowControl(searchDepth=1,Name="无标题 - 记事本")
notepad.MoveToCenter()
time.sleep(2)
notepad.ButtonControl(Name="关闭").Click()




