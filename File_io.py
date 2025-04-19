# function to read data file:
from microbit import *
def get_nv_data(name):
    try:
        with open(name) as f:
            v = int(f.read())
    except OSError:
        v = temperature()
        try:
            with open(name, 'w') as f:
                f.write(str(v))
        except OSError:
            display.scroll('Cannot create file %s' % name)

    except ValueError:
        display.scroll('invalid data in file %s' % name)
        v = temperature()

    return v

# function to write data file:
def append_data(filename, value):
    try:
        with open(filename, 'w') as f:
            f.write(str(value))
    except OSError:
        display.scroll('Cannot write to file %s' % filename)
        print('Cannot write to file %s' % filename)