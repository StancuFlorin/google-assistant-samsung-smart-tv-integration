#!/usr/bin/env python

from devicehub.devicehub import Actuator, Device, Project
import commands, config
import samsungctl

first_time = True
def process_event(data):
    global first_time
    if first_time:
        first_time = False
        return None        

    command_id = int(event.state)
    print 'Command ', event.state, ' was received'
    remote = samsungctl.Remote(config.REMOTE)
    
    if (command_id < 200):
        commands.change_channel(event.state, remote)
    else:
        command = commands.dictionary[event.state]
        if command is not None:
            print 'The custom command ', event.state, ' will run'
            command(remote)
        else:
            print 'There is no custom command implemented for ', event.state

project = Project(config.PROJECT_ID, persistent = False)
device = Device(project, config.DEVICE_UUID, config.API_KEY)

event = Actuator(Actuator.ANALOG, 'change_channel')
device.addActuator(event, process_event)

while True:
    pass
