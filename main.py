from microbit import *
import log
import radio
log.set_labels('temperature')

radio.config(group=23)
radio.on()
Filename = 'Temperature.txt'
while True:
    message = radio.receive()
    if message:
        print(str(message))
        display.scroll(str(message))
#        append_data(Filename, message)
        log.add({'temperature':message})
        sleep(200)