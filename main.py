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
        display.show('Clear')

    message = radio.receive()
    if message:
#        print(str(message))
        display.scroll(message)
        log.add({'temperature':message})
        
    if button_a.was_pressed():    
        Loop_ctrl = False 
        display.clear()