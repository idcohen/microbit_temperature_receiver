from microbit import *
import log
import radio

log.set_labels('temperature')

radio.config(group=55)
radio.on()

display.clear()

Loop_Ctrl_b = True
while Loop_Ctrl_b:
    Loop_Ctrl_a = True
    if button_a.was_pressed():
        log.delete(full=True)
#        display.show('Log Clear')
        display.show('Listening')
        while Loop_Ctrl_a:
            message = radio.receive()
            if message:
        #        print(str(message))
                display.scroll(message)
                log.add({'temperature':message})
            
            if button_b.was_pressed():
                display.show('Radio Off')
                Loop_Ctrl_a = False
                Loop_Ctrl_b = False
                radio.off()
                display.scroll('Log Stored')
                display.clear()