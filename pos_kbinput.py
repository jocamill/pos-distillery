# notes  pip install pynut
# https://pypi.org/project/pynput/



from pynput import keyboard

def on_press(key):
# attempt to catch the hand scanner input and stack the str

    try:         
       #print('alphanumeric key {0} pressed'.format(key.char))
       print('Scanning DL *********************************')

    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if key == keyboard.Key.enter:
            print('The ENTER was pressed')

def on_release(key):
#   print('{0}'.format(key))
#   inputstr = "" + '{0}'.format(key)    
    if key == keyboard.Key.esc:
        # Stop listener
        print('Exiting by command')
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

def main():
    def on

