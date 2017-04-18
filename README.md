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
- create a free account on [devicehub.net](https://www.devicehub.net)
- create a project on devicehub.net (ex: Samsung Remote)
- add a device on the respective project (ex: Raspberry Pi)
- add an actuator on the respective device (ex: samsung_smart_tv_remote)

### Locally ###

- You need to create a file named ``config.py``. There is an example on ``config.py.example``.
- To enable to comunication with your TV you will need to put the correct IP on ``REMOTE.host``. Your TV should be on the same network with the PC that will run this script. If you have an older TV (<2016) you will need to change the method and the port also. Check [samsungctl](https://github.com/Ape/samsungctl) for more information.
- The DeviceHub information also needs to be added. Make sure that you add the correct data there.

## Make the script start at startup ##

You may want to make the script start each time you boot your Raspberry Pi. There are several ways how to do it. Here is one.

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

