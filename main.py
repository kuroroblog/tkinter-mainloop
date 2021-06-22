import tkinter as tk

# Windowを取得する。
def getWindow(root):
    # Windowに対してmainloop関数を呼ぶ。
    root.mainloop()

# Frameを取得する。
def getFrame(root):
    # Windowを親要素として、frame Widget(Frame)を作成する。
    # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
    frame = tk.Frame(root)
    # Frameに対してmainloop関数を呼ぶ。
    frame.mainloop()

# Widgetを取得する。
def getWidget(root):
    # Windowを親要素として、frame Widget(Frame)を作成する。
    # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
    frame = tk.Frame(root)

    # frame Widget(Frame)を親要素として、text Widgetを作成する。
    # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
    text = tk.Text(frame)
    # Widgetに対してmainloop関数を呼ぶ。
    text.mainloop()

# 足し算を行う関数
# 第一引数 : number
# 第二引数 : number
# 戻り値 : number
def calcPlus(preNum, nextNum):
    return preNum + nextNum

# helloをloopする関数
def getLoop():
    while True:
        print('hello')

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
    # getWindow(root)
    # getFrame(root)
    # getWidget(root)
    # print(calcPlus(1, 5))
    # getLoop()
