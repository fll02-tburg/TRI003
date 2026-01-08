from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor

# Set up all devices.
hub = PrimeHub()
motor = Motor(Port.C, Direction.CLOCKWISE)

# The main program starts here.
# USE THIS TO ZERO OUT THE GYRO AND PREP THE ROBOT FOR COMPETITION
print('Hello, World!')
for count in range(3):
    hub.light.on(Color.RED)
    wait(100)
    hub.light.on(Color.GREEN)
    wait(100)
    hub.speaker.beep(500, 100)
    wait(100)

