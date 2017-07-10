# Google Home - Samsung Smart TV Integration #

Use your Google Home device as a remote for your Samsung Smart TV. There is no need for a Logitech Harmony device.

![Integration Flow](https://raw.githubusercontent.com/StancuFlorin/Google-Home-Samsung-Smart-TV-Integration/pic/flow.png "Integration Flow")

## Requirements ##

- Python 2.7
- ``# pip install -r requirements.txt``

## Installation ##

### CloudAMQP ###
- Create a free account on [CloudAMQP](https://www.cloudamqp.com).
- Create a new instance. The free plan is enough.
- Go to the RabbitMQ Manager.
- Add a new ``exchange``:
	- name: ``google.home.assistant``
	- type: ``direct``
- Add a new ``queue``:
	- name: ``samsung.smart.tv``
	- arguments: ``Message TTL`` with the value of ``30000``. The name of this feature is ``x-message-ttl``
- Go back to the exchange that you created and add a binding to the queue:
	- name: ``samsung.smart.tv``
	- routing key: ``samsung.smart.tv``

### Locally ###

- Check the ``config.ini`` file and add your own details there.
- To enable to comunication with your TV you will need to put the correct IP on ``SamsungSmartTV.host``. Your TV should be on the same network with the PC that will run this script. If you have an older TV (<2016) you will need to change the method and the port also. Check [samsungctl](https://github.com/Ape/samsungctl) for more information.
- The CloudAMQP information also needs to be added. Make sure that you add the correct data there.
- Run the script using ``python samsung-smart-tv-remote.py`` or ``./samsung-smart-tv-remote.py``

### IFTTT ###

- Create a new applet on [IFTTT](https://ifttt.com).
- On ``this`` select ``Google Assistant`` and ``Say a simple phrase`` from there.
- Add a phrase. Use only lower case letters (ex: change the channel on hbo).
- On ``that`` select ``Maker Webhooks`` and ``Make a web request`` from there.
- On URL add ``https://pspeaemf:ByOti2ToHWya_dV79B85GaDZaORBpi3L@lark.rmq.cloudamqp.com/api/exchanges/pspeaemf/google.home.assistant/publish``. Change the username, password and the RabbitMQ host with your own.
- Select ``POST`` method and ``application/json`` as content type.
- On body add ``{ "properties": { "content-type": "application/json" }, "routing_key": "samsung.smart.tv", "payload": "{\"command\": \"CHANGE_CHANNEL\", \"value\": \"135\"}", "payload_encoding": "string" }``. 135 is the channel number for HBO. You can add different applets like this for whatever channel you want and the only thing that you need to change is the the ``value`` node. You can also use custom commands like ``turn off the tv``, but you need to change the ``command`` node like in this example ``{ "properties": { "content-type": "application/json" }, "routing_key": "samsung.smart.tv", "payload": "{\"command\": \"TURN_OFF\"}", "payload_encoding": "string" }``

## Custom Commands ##

Here is the list of the custom commands implemented so far.

Command Code | Command Description
------------ | -------
TURN_OFF | Turn off the TV

## Make the script start at startup ##

If you use a Raspberry Pi to run this script you may want to make it start each time you boot your device. There are several ways how to do it. Here is one.

``
$ sudo chmod +x /path/to/your/script/samsung-smart-tv-remote.py
``

``
$ sudo nano /etc/rc.local
``

Before ``exit 0`` put the below line. This will start the script 15 seconds after the device is up.

``
/bin/sleep 15 && /path/to/your/script/samsung-smart-tv-remote.py &
``

``
sudo reboot
``

## Tested Devices ##

- Samsung UE49K5502
