# Google Home - Samsung Smart TV Integration #

Use your Google Home device as a remote for your Samsung Smart TV. There is no need for a Logitech Harmony device.

![Integration Flow](https://raw.githubusercontent.com/StancuFlorin/Google-Home-Samsung-Smart-TV-Integration/pic/flow.png "Integration Flow")

## Requirements ##

- Python 2.7
- ``pip install websocket-client``
- [samsungctl](https://github.com/Ape/samsungctl) ``pip install samsungctl``
- ``pip install httplib2 paho-mqtt``
- [devicehub](https://github.com/devicehubnet/devicehub_py) ``pip install devicehub``

## Installation ##

### DeviceHub ###
- Create a free account on [DeviceHub](https://www.devicehub.net).
- Create a project on DeviceHub.
- Add a device on the respective project.
- Add an actuator on the respective device (ex: samsung_smart_tv_remote).

### Locally ###

- You need to create a file named ``config.py``. There is an example on ``config.py.example``.
- To enable to comunication with your TV you will need to put the correct IP on ``REMOTE.host``. Your TV should be on the same network with the PC that will run this script. If you have an older TV (<2016) you will need to change the method and the port also. Check [samsungctl](https://github.com/Ape/samsungctl) for more information.
- The DeviceHub information also needs to be added. Make sure that you add the correct data there.
- Run the script using ``python samsung-remote.py`` or ``./samsung-remote.py``

### IFTTT ###

- Create a new applet on [IFTTT](https://ifttt.com).
- On ``this`` select ``Google Assistant`` and ``Say a simple phrase`` from there.
- Add a phrase. Use only lower case letters (ex: change the channel on hbo).
- On ``that`` select ``Maker Webhooks`` and ``Make a web request`` from there.
- On URL add ``https://api.devicehub.net/v2/project/YOUR_PROJECT_ID/device/YOUR_DEVICE_UUID/actuator/samsung_smart_tv_remote/state``
- Select ``POST`` method and ``application/json`` as content type.
- On body add ``{"state":"135","apiKey":"YOUR_API_KEY"}``. 135 is the channel number for HBO. You can add different applets like this for whatever channel you want and the only thing that you need to change is the value for the ``state`` node. If the value of the state node is less than 200 the command will be considered as a channel number. For custom commands like ``turn off the tv`` use numbers higher than 200.

## Custom Commands ##

Actuator State | Command
-------------- | -------
201 | Turn off the TV

You can add your custom commands on ``commands.py`` file.

## Make the script start at startup ##

If you use a Raspberry Pi to run this script you may want to make it start each time you boot your device. There are several ways how to do it. Here is one.

``
$ sudo chmod +x /path/to/your/script/samsung-remote.py
``

``
$ sudo nano /etc/rc.local
``

Before ``exit 0`` put the below line. This will start the script 15 seconds after the device is up.

``
/bin/sleep 15 && /path/to/your/script/samsung-remote.py &
``

``
sudo reboot
``

## Tested Devices ##

- Samsung UE49K5502
