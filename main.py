from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    message = radio.receive()
    sleep(200)
   # print(message)
    #message = "hello"
    display.scroll(str(message))