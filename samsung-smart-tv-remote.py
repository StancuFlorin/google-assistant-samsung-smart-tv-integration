#!/usr/bin/env python

import configparser, pika, json, samsungctl

config = configparser.ConfigParser()
config.read('config.ini')

params = pika.URLParameters(config['CloudAMQP']['url'])
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel

REMOTE = {
    "name": config['SamsungSmartTV']['name'],
    "description": config['SamsungSmartTV']['description'],
    "id": "",
    "host": config['SamsungSmartTV']['host'],
    "port": int(config['SamsungSmartTV']['port']),
    "method": config['SamsungSmartTV']['method'],
    "timeout": 0
}

def change_channel(channel, remote):
	for digit in channel:
		remote.control("KEY_" + digit)
	remote.control("KEY_ENTER")
	print 'The channel was changed to ', channel

def turn_off_tv(remote):
    print 'The TV is shutting down'
    remote.control("KEY_POWER")
	
# create a function which is called on incoming messages
def callback(ch, method, properties, body):
	message = json.loads(body)
	remote = samsungctl.Remote(REMOTE)
	
	if message['command'] == "CHANGE_CHANNEL":
		change_channel(message['value'], remote)
	elif message['command'] == "TURN_OFF":
		turn_off_tv(remote)
	else:
		print 'There is no custom command implemented for ', message['command']
		
# set up subscription on the queue
channel.basic_consume(callback, queue=config['CloudAMQP']['queue'], no_ack=True)

print "Waiting for commands"
channel.start_consuming() # start consuming (blocks)

connection.close()