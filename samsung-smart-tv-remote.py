import configparser
import pika
import json
import time
from samsungtvws import SamsungTVWS

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Setup CloudAMQP connection
params = pika.URLParameters(config['CloudAMQP']['url'])
params.socket_timeout = 5
connection = pika.BlockingConnection(params)  # Connect to CloudAMQP
channel = connection.channel()  # Start a channel

# Samsung TV configuration
config_remote = {
    "host": config['SamsungSmartTV']['host'],
    "port": int(config['SamsungSmartTV']['port']),
    "timeout": 0,
}

# Function to change the TV channel
def change_channel(channel_number):
    with SamsungTVWS(host=config_remote['host'], port=config_remote['port']) as remote:
        for digit in str(channel_number):
            print(f"Sending digit: {digit}")
            remote.send_key(f"KEY_{digit}")
            time.sleep(0.5)
        remote.send_key("KEY_ENTER")
        print(f"Channel changed to {channel_number}")

# Function to turn off the TV
def turn_off_tv():
    with SamsungTVWS(host=config_remote['host'], port=config_remote['port']) as remote:
        print("Shutting down the TV")
        remote.send_key("KEY_POWER")

# Callback function for incoming messages
def callback(ch, method, properties, body):
    message = json.loads(body)
    command = message.get('command')
    value = message.get('value')

    if command == "CHANGE_CHANNEL":
        change_channel(value)
    elif command == "TURN_OFF":
        turn_off_tv()
    else:
        print(f"No command implemented for: {command}")

# Set up subscription to the queue
channel.basic_consume(
    queue=config['CloudAMQP']['queue'],
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for commands...")
channel.start_consuming()  # Start consuming (blocks)

connection.close()
