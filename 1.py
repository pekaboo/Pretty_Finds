# import asyncio
# from playwright import async_playwright


# async def run_demo():
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         page = await browser.new_page()

#         # 打开网页
#         await page.goto('https://example.com')

#         # 截图
#         await page.screenshot(path='screenshot.png')

#         # 获取页面标题
#         title = await page.title()
#         print(f"Page title: {title}")

#         # 获取页面内容
#         content = await page.content()
#         print(f"Page content: {content}")

#         # 关闭浏览器
#         await browser.close()


# # 运行示例
# asyncio.run(run_demo())


import pyautogui
import time

# 打开微信的快捷键 
# pyautogui.hotkey('ctrl', 'alt', 'w') 
# time.sleep(3) 



# 在搜索框中输入指定联系人的名字
pyautogui.typewrite('联系人的名字') 
time.sleep(3) 

# 按下键盘的 "down" 键选中联系人后，按 "enter" 键进入对话窗口
pyautogui.press('down') 
pyautogui.press('enter')
time.sleep(2) 

# 输入你要发送的消息
pyautogui.typewrite('你想要发送的消息')

# 按 "enter" 键发送
pyautogui.press('enter') 