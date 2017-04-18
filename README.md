# Rasberry Pi Samsung TV Remote #

TBA

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

