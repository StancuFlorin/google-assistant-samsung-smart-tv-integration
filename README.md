# Google Home - Samsung Smart TV Integration #

Use your Google Home device as a remote for your Samsung Smart TV. There is no need for a Logitech Harmony device.

![Integration Flow](https://raw.githubusercontent.com/StancuFlorin/Google-Home-Samsung-Smart-TV-Integration/pic/flow.png "Integration Flow")

## Requirements ##

- Python 2.7
- ``pip install websocket-client``
- [samsungctl](https://github.com/Ape/samsungctl) ``pip install samsungctl``
- ``pip install httplib2 paho-mqtt``
- [devicehub](https://github.com/devicehubnet/devicehub_py) ``pip install devicehub``

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

