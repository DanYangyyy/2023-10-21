from pynput import keyboard
from playsound import playsound
count = 0
def onRelease(key):
    """
    此函数，就是用户释放键盘按键的时候，就会被调用到
    :param key: 用户调用哪个键
    """
    print(key)
    global count
    count += 1
    if count % 10 == 0:
        #播放音频
        playsound('sound/1.mp3')


listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()
#bianxieygdaimabiBXDHBJS
#编写