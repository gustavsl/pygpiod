# pygpiod

## A simple Python wrapper for the libgpiod Python bindings

The libgpiod Python bindings are not very straightforward to use and they lack proper documentation.

I've created this simple library to provide an easy-to-use interface to those libs.

## Examples

### GPIO write

```python
from gpio import GPIO
import time

myGpio = GPIO()

myGpio.setup("SODIMM 138", GPIO.OUT)

myGpio.write(GPIO.HIGH)

time.sleep(1)

myGpio.write(GPIO.LOW)
```
