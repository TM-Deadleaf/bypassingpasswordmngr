import win32clipboard
import time
while True:
    win32clipboard.OpenClipboard()
    data=win32clipboard.GetClipboardData()
    with open("clipboard.txt",'a+') as f:
        f.write(data)
    time.sleep(5)