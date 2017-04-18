def change_channel(channel, remote):
    for digit in channel:
        remote.control("KEY_" + digit)
    remote.control("KEY_ENTER")
    print 'The channel was changed to ', channel
    
def turn_off_tv(remote):
    print 'The TV is shutting down'
    remote.control("KEY_POWER")

def set_external_speaker(remote):
    print 'The audio output was set to optical'

dictionary = {"201": turn_off_tv, "202": set_external_speaker}
