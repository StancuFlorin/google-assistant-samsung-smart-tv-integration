#!/usr/bin/env python

import configparser, pika, json, time, samsungctl

config = configparser.ConfigParser()
config.read('config.ini')

params = pika.URLParameters(config['CloudAMQP']['url'])
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel

config_remote = {
    "name": config['SamsungSmartTV']['name'],
    "description": config['SamsungSmartTV']['description'],
    "id": "",
    "host": config['SamsungSmartTV']['host'],
    "port": int(config['SamsungSmartTV']['port']),
    "method": config['SamsungSmartTV']['method'],
    "timeout": 0
}

def change_channel(channel):
	with samsungctl.Remote(config_remote) as remote:
		for digit in channel:
			print "working on", digit
			remote.control("KEY_" + digit)
			time.sleep(0.5)
		remote.control("KEY_ENTER")
		print "The channel was changed to", channel

def turn_off_tv():
	with samsungctl.Remote(config_remote) as remote:
		print "The TV is shutting down"
		remote.control("KEY_POWER")
	
# create a function which is called on incoming messages
def callback(ch, method, properties, body):
	message = json.loads(body)
	
	if message['command'] == "CHANGE_CHANNEL":
		change_channel(message['value'])
	elif message['command'] == "TURN_OFF":
		turn_off_tv()
	else:
		print "There is no custom command implemented for", message['command']
		
# set up subscription on the queue
channel.basic_consume(callback, queue=config['CloudAMQP']['queue'], no_ack=True)

#print "Waiting for commands"
channel.start_consuming() # start consuming (blocks)

connection.close()
