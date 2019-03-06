# coding: utf-8
import traceback
from wxpy import *
import random
from threading import Timer
def send_news():
    contents = ["来催啦",'求传','记得传网盘哦','又是来催传的一天','求传谢谢小筷']
    # contents = ["测试微信机器人1", '测试微信机器人2', '测试微信机器人3', '测试微信机器人4', '测试微信机器人5']
    try:

        bot = Bot( cache_path=True)

        my_friend = bot.friends().search(u'严新成')[0]
        i = random.randint(0,4)
        my_friend.send(contents[i])
        t = Timer(86400, send_news)
        t.start()
    except:
        traceback.print_exc()
        bot.self.send("今天发送失败来")

if __name__ == "__main__":
    send_news()