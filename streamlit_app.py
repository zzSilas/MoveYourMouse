import streamlit as st
if st.button("ShakeShake!!"):
    import pyautogui
    import time
    pyautogui.FAILSAFE = False
    while True:
        pyautogui.moveRel(10, 0)  # 向右移动10个像素
        time.sleep(1)           # 等待0.1秒
        pyautogui.moveRel(-10, 0) # 向左移动10个像素
        time.sleep(1)           # 等待0.1秒
    st.success(f"Ready!")
