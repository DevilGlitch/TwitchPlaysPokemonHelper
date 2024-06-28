import keyboard
import time

last_processed_key = None

def clear_chatbox():
    keyboard.send('ctrl+a')
    keyboard.send('backspace')

def ShadyTwitchPokemonHelper(event):
    global last_processed_key
    
    key_name = event.name.lower()  # Convert to lowercase for case insensitivity
    
    commands = {
        "up": "!up",
        "down": "!down",
        "left": "!left",
        "right": "!right",
        "z": "!a",
        "x": "!b",
        "c": "!select",
        "a": "!x",
        "s": "!y",
        "d": "!start"
    }
    
    if event.event_type == keyboard.KEY_DOWN and key_name in commands:
        last_processed_key = key_name
        clear_chatbox()
        time.sleep(0.05)
        keyboard.write(commands[key_name])
        keyboard.send('enter')

    elif event.event_type == keyboard.KEY_UP and key_name == last_processed_key:
        last_processed_key = None

keyboard.hook(ShadyTwitchPokemonHelper)

keyboard.wait('esc')
