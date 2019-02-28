#  Test file for keyboard input.   moved to main.py
# https://pypi.org/project/pynput/

from pynput import keyboard

keys= []

def on_press(key):
    try: 
        k = key.char # single-char keys
        keys.append(k) 
        print('Key pressed: ' + k)    
    except: 
        k = key.name # other keys
        if key == keyboard.Key.esc: return False # stop listener
    
lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
print(keys)
