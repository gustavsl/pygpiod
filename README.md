# pygpiod

## A simple Python wrapper for the libgpiod Python bindings

The libgpiod Python bindings are not very straightforward to use and they lack proper documentation besides the examples.

I've created this simple library to provide an easy-to-use interface to those libs.

This library also makes it easier to set up and use a GPIO by its line-name instead of gpiochip lines/offsets.

## Examples

### GPIO write

```python
from gpio import GPIO
import time

myGpio = GPIO()

# Get the GPIO by its gpio-line-name on the device tree!

# Setting up GPIO on SODIMM 138 on a Toradex Colibri module
myGpio.setup("SODIMM_138", GPIO.OUT)

# Example: Setting up GPIO on GPIO22 on a Raspberry Pi 3
# myGpio.setup("GPIO22", GPIO.OUT)

myGpio.write(GPIO.HIGH)

time.sleep(1)

myGpio.write(GPIO.LOW)
```

### GPIO write & read

```python
from gpio import GPIO
import time

myGpio = GPIO()

# Get the GPIO by its gpio-line-name on the device tree!

# Setting up GPIO on SODIMM 138 on a Toradex Colibri module
myGpio.setup("SODIMM_138", GPIO.OUT)

# Example: Setting up GPIO on GPIO22 on a Raspberry Pi 3
# myGpio.setup("GPIO22", GPIO.OUT)

myGpio.write(GPIO.HIGH)
print(myGpio.read())

time.sleep(1)

myGpio.write(GPIO.LOW)
print(myGpio.read())

time.sleep(1)
```
