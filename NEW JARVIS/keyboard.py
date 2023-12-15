from pynput.keyboard import Key,Controller
import screen_brightness_control as sbc

from time import sleep
import ctypes

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


#def brightness_up():
#    # Simulate pressing the brightness up key multiple times
#    global i
#    if i > 101:
#       i=10
#       sbc.set_brightness(i)
#    else:
#        sbc.set_brightness(i)
#    i=i+10
#
#def brightness_down():
#    # Simulate pressing the brightness down key multiple times
#    sbc.fade_brightness(50)


