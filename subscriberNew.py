import subprocess
from adafruit_servokit import ServoKit
import paho.mqtt.client as mqtt

# Initialize the ServoKit instance
kit = ServoKit(channels=16)

# MQTT Broker settings
MQTT_BROKER = "localhost"  # Change this to your MQTT broker address
MQTT_PORT = 1883
MQTT_TOPIC = "drone/control"  # Change this to your MQTT topic

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")

    # Check if the message is a coordinate message (e.g., 'x,y,z')
    if ',' in message:
        try:
            # Parse the x, y, z values
            x, y, z = map(int, message.split(','))  # Assuming the message format is 'x,y,z'
            # Set the servo angles
            kit.servo[0].angle = x  # Servo for X
            kit.servo[1].angle = y  # Servo for Y
            print(f"Set servo 0 to {x} degrees, servo 1 to {y} degrees")
        except ValueError as e:
            print(f"Error processing coordinate message: {e}")
    else:
        # Handle gamepad commands
        execute_drone_command(message)

def execute_drone_command(command):
    print(f"Executing command: {command}")
    if command == "DPAD_left":
        subprocess.run(["python3", "AileronsDraftLeft.py"])
    elif command == "DPAD_right":
        subprocess.run(["python3", "AileronsDraftRight.py"])
    elif command == "DPAD_up":
        subprocess.run(["python3", "AileronsDraftUp.py"])
    elif command == "DPAD_down":
        subprocess.run(["python3", "AileronsDraftDown.py"])
    else:
        print(f"Unknown Command: {command}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
