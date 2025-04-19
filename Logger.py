from microbit import *
import log

#log.set_labels('temperature', 'sound', 'light')

#log.add({
#  'temperature': temperature(),
#  'sound': microphone.sound_level(),
#  'light': display.read_light_level()
#})

def append_log(sensor,value):
    log.add({
    sensor: value
})
    