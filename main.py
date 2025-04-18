from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    message = radio.receive()
    if message:
        print(str(message))
        display.scroll(str(message))
        sleep(200)