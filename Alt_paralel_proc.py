from multiprocessing import Process
from pynput import keyboard
from time import sleep

class A:
    def __call__(self,sleep_time):
        while 1:
            print ('i do some thing')
            sleep(sleep_time)

coldown=5
start = '1'
stop = '2'
p1 = Process(target=A(), args={coldown})

#When key =start was pressed we start process if key=stop was pressed we stop process or if start==stop we wait second pressed for stop process

def on_press(key):
    global p1
    if p1.is_alive() == False:
        p1 = Process(target=A(), args={coldown})
    try:
        c=key.char
    except AttributeError:
        c=format(key)
    if c == start and p1.is_alive() == False:
        p1.start()
    elif c == stop and p1.is_alive() == True:
        p1.terminate()

#Start listner
if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

