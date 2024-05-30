from time import sleep
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# Set both servos to initial position
kit.servo[0].angle = 90
kit.servo[1].angle = 90  # Assuming you want to control servo 1 as well

sleep(3)

# Move both servos to 180 degrees
kit.servo[0].angle = 0
kit.servo[1].angle = 180  # Move servo 1 to 180 degrees simultaneously

sleep(3)

# Return both servos to 0 degrees
kit.servo[0].angle = 90
kit.servo[1].angle = 90  # Move servo 1 back to 0 degrees simultaneously
