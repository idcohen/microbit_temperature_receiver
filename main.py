from microbit import *
import log
import radio

log.set_labels('temperature')

radio.config(group=55)
radio.on()

log.delete(full=True)
display.show('Log Clear')
display.clear()

Loop_Ctrl_b = True
while Loop_Ctrl_b:
    Loop_Ctrl_a = True
    if button_a.was_pressed():
        while Loop_Ctrl_a:
            message = radio.receive()
            if message:
        #        print(str(message))
                display.scroll(message)
                log.add({'temperature':message})
            
            if button_b.was_pressed():
                Loop_Ctrl_a = False
                Loop_Ctrl_b = False
                radio.off()


        
        # @run_every(s=30)
       # def log_data():
        #    log.add({
        #      'temperature': temperature(),
        #      'sound': microphone.sound_level(),
        #      'light': display.read_light_level()
        #    })
            
        #while True:
        #    sleep(100000)
        