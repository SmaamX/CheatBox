#PyCPS Beta
print ('Loading...')
try:
    import pyautogui
except ModuleNotFoundError:
    print ('pip install pyautogui')
try:
    import colorama
    print(colorama.Fore.GREEN + "RIP Technoblade")
except ModuleNotFoundError:
    print("RIP Technoblade")
try:
    import keyboard
    from keyboard import is_pressed as ip
except ModuleNotFoundError:
    print ('pip install keyboard')
from time import sleep as sl
from random import randint as ri
pyautogui.PAUSE = 0
print('Start')
LBM = input('Jitter (Y/N):')
LBM = True if any(x.lower() in ['y', 'yes'] for x in LBM) else False
if LBM == True: print ('on')
else: print ('off')
#
def randx(x,y,z,ax,x0,y0,z0,a0,x1,y1,z1,a1,x2,y2,z2,a2,x3,y3,z3,a3,x4,y4,z4,a4,x5,y5,z5,a5,h2):
    if LBM == False:
        a = grandom(x2,y2,z2,a2)
        g = grandom(x3,y3,z3,a3)
    elif LBM == True:
        a = grandom(x4,y4,z4,a4)
        g = grandom(x5,y5,z5,a5)
    m = grandom(x,y,z,ax)
    m1 = grandom(x0,y0,z0,a0)
    m2 = grandom(x1,y1,z1,a1)
    if a > h2 and not a/m2-g+m-m1 <= 0:
        a = a/m2-g+m-m1
    elif a-g <= 0:
        a = (g-a+m)*(m1/m2)+m2
    elif a < h2 and not a/m2-g-m+(m1/2) <= 0:
        a = a/m2-g-m+(m1/2)
    else: a = (a+g-m)*(m1/m2)+m2
    return a
#
def cooldown(a,b,c,d):
    if LBM == True:
        p = ri(a,b)
    elif LBM == False:
        p = ri(c,d)
    if p == 1:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -1
        sl(coold)
    elif p == 20:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -2
        sl(coold)
    elif p == 25:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -3
        sl(coold)
    elif p == 30:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -2
        sl(coold)
    elif p == 35:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -3
        sl(coold)
    elif p == 40:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -1
        sl(coold)
#
def grandom(x,y,z,a):
    d = ri(1,2)
    if d == 1:
        r1 = ri(x,y)
        ri2 = ri(z,a)
        r = ri(r1,ri2)
    else:
        r1 = ri(z,a)
        ri2 = ri(x,y)
        r = ri(ri2,r1)
    return r
try:
    h1 = 0
    h2 = 0
    def start():
        global h1
        global LBM
        cooldown(1,65,1,40)
        p = randx(2,5,6,8,1,2,3,4,2,3,4,5,35,52,53,206,12,24,25,91,2,10,20,21,9,11,25,26,h1)
        h1 = p
        p = p * 10 ** -3
        sl(p)
        pyautogui.leftClick()
#
    def start2():
        global h2
        global LBM
        cooldown(1,65,1,40)
        p = randx(2,5,6,8,1,2,3,4,2,3,4,5,10,30,31,102,12,24,25,26,7,21,22,24,12,24,25,26,h2)
        h2 = p
        p = p * 10 ** -3
        sl(p)
        pyautogui.rightClick()
    def on_start_pressed():
        start()
    def on_start2_pressed():
        start2()
    def on_stop_pressed():
        print('Stop')
        sl (1)
        while True:
            if keyboard.is_pressed('y'):
                print('Restart')
                sl (1)
                break
    def fixkey (x,y,rt):
        keyboard.add_hotkey(x +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x, rt)
#
    def fixkey3 (x,y,z,rt):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(z+'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x, rt)
#
    def fixkey4 (x,y,z,s,rt):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z +'+'+ s, rt)
        keyboard.add_hotkey(x +'+'+ y +'+'+ s +'+'+ z, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(s +'+'+ x +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ x +'+'+ y +'+'+ s, rt)
        keyboard.add_hotkey(z +'+'+ x +'+'+ s +'+'+ y, rt)
        keyboard.add_hotkey(z +'+'+ s +'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(s +'+'+ z +'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y +'+'+ s, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ s +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(s +'+'+ x +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z +'+'+ s, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ s +'+'+ z, rt)
        keyboard.add_hotkey(y +'+'+ s +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(s +'+'+ y +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ s +'+'+ x, rt)
        keyboard.add_hotkey(z +'+'+ s +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(s +'+'+ z +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ s +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ s +'+'+ z +'+'+ x, rt)
        keyboard.add_hotkey(s +'+'+ y +'+'+ z +'+'+ x, rt)
#
    def fixkey5(x,r,s,rt):
        keyboard.add_hotkey(x +'+'+ r +'+'+ s, rt)
        keyboard.add_hotkey(s+'+'+ x +'+'+ r, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ r, rt)
        keyboard.add_hotkey(r +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(s +'+'+ r +'+'+ x, rt)
        keyboard.add_hotkey(r +'+'+ s +'+'+ x, rt)
#  
    def mkey(x,y,z,a,r,s,rt):
        fixkey (x,r,rt)
        fixkey (y,r,rt)
        fixkey (a,r,rt)
        fixkey (z,r,rt)
        fixkey (s,r,rt)
        fixkey3 (x,y,r,rt)
        fixkey3 (x,a,r,rt)
        fixkey3 (x,z,r,rt)
        fixkey3 (y,z,r,rt)
        fixkey3 (y,a,r,rt)
        fixkey3 (a,z,r,rt)
        fixkey5 (x,r,s,rt)
        fixkey5 (y,r,s,rt)
        fixkey5 (z,r,s,rt)
        fixkey5 (a,r,s,rt)
        fixkey4 (x,y,r,s,rt)
        fixkey4 (x,a,r,s,rt)
        fixkey4 (x,z,r,s,rt)
        fixkey4 (y,z,r,s,rt)
        fixkey4 (y,a,r,s,rt)
        fixkey4 (a,z,r,s,rt)
    def tomkey (x,y,z,a,r,s,c,sh,rt):
        mkey(x,y,z,a,r,s,rt)
        mkey(x,y,z,c,r,s,rt)
        mkey(x,y,z,a,r,c,rt)
        mkey(x,y,z,sh,r,s,rt)
        mkey(x,y,z,a,r,sh,rt)
    tomkey ('w','a','s','d','r','space','ctrl','shift',on_start_pressed)
    tomkey ('w','a','s','d','f','space','ctrl','shift',on_start2_pressed)
    keyboard.add_hotkey('r', on_start_pressed)
    keyboard.add_hotkey('f', on_start2_pressed)
    keyboard.add_hotkey('y', on_stop_pressed)
    keyboard.wait()
except KeyboardInterrupt:
    print ('Force stop')