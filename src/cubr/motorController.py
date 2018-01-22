import serial

class motorController:
# TODO: in the future, this could be made smarter eg:
#   - configurable speed/acceleration of the arduino motor controller.
#   - Ack from the arduino to confirm move completion. This would be used to
#       allow the GUI to be smarter (update the current state automatically, etc)

    def __init__(self):
        # TODO This should probably be configurable from the GUI/settings menu
        self.serialPort = "/dev/ttyACM0"
        self.serialBaudRate = 9600

        self.serialDevice = serial.Serial(self.serialPort, self.serialBaudRate)

    def sendString(self, solutionString):

        # Workaround for motorController falling over if string does not end
        # with space
        if (not solutionString.endswith(' ')):
            solutionString += ' '

        self.serialDevice.write(solutionString)

