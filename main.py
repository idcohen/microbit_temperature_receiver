from microbit import *
import log
import radio
log.set_labels('temperature')

radio.config(group=23)
radio.on()
Filename = 'Temperature.txt'
log.delete()
#@run_every()

while True:
    message = radio.receive()
    if message:
        print(str(message))
        display.scroll(str(message))
#        append_data(Filename, message)
        log.add({'temperature':message})
        sleep(200)

        @run_every(s=30)
        def log_data():
            log.add({
              'temperature': temperature(),
              'sound': microphone.sound_level(),
              'light': display.read_light_level()
            })
            
        while True:
            sleep(100000)
        