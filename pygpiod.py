import gpiod

class GPIO(object):

    OUT = gpiod.LINE_REQ_DIR_OUT
    IN = gpiod.LINE_REQ_DIR_IN
    HIGH = 1
    LOW = 0

    def __init__(self):
        self.line = None
        self.chip = None
        self.offset = None
        self.offsetList = []
        self.pin = None

    def setup(self, line, direction):
        self.chip = gpiod.find_line(str(line)).owner().name()
        self.offset = gpiod.find_line(str(line)).offset()
        self.offsetList.append(self.offset)
        self.pin = gpiod.Chip(self.chip).get_lines(self.offsetList)
        self.pin.request(consumer=self.chip, type=direction)

    def write(self, level):
        valuesList = []
        valuesList.append(level)
        self.pin.set_values(valuesList)

    def read(self):
        return self.pin.get_values()[0]
