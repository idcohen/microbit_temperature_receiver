from microbit import *
import log
import radio

log.set_labels('temperature')

radio.config(group=55)
radio.on()

Loop_ctrl = True
while Loop_ctrl:
    if button_b.was_pressed():
        log.delete(full=True)
        display.scroll('Log Cleared')

    message = radio.receive()
    if message:
        print(str(message))
        display.scroll(str(message))
        log.add({'temperature':message})
        
    if button_a.was_pressed():    
        Loop_ctrl = False   




        
        # @run_every(s=30)
       # def log_data():
        #    log.add({
        #      'temperature': temperature(),
        #      'sound': microphone.sound_level(),
        #      'light': display.read_light_level()
        #    })
            
        #while True:
        #    sleep(100000)
        