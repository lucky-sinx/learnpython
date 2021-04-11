from pywinauto import application,Application
import time
import subprocess,uiautomation
import os
subprocess.Popen('calc.exe')
# os.system('calc.exe') # 不建议，开启子线程

#创建窗口
calc_window=uiautomation.WindowControl(searchDepth=1,Name="计算器")
calc_window.SetTopmost(True)
calc_window.MoveToCenter()
# calc_window.SetActive(0.1)

#模拟按钮点击
# uiautomation.ButtonControl()
calc_window.ButtonControl(Name='八').Click()
calc_window.ButtonControl(Name='加').Click()
calc_window.ButtonControl(Name='九').Click()
calc_window.ButtonControl(Name='等于').Click()

#