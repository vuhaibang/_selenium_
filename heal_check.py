import os
import time


while True:
    with open("/home/vuhaibangtk/test.txt", "r+") as f:
        data = f.read()
        data = int(data)
    if time.time() - data > (5 * 60):
        print(time.time() - data)
        print("crash")
        os.system('kill -9 $(ps -x | grep firefox)')
        os.system('kill -9 $(ps -x | grep chrome)')
        os.system('tmux send-keys -t ytb:view Enter "cd /home/vuhaibangtk/_selenium_" Enter "python3.8 app.py" Enter')
    time.sleep(5*60)