# dht22
Send data from DHT22 to ThingSpeak using a Raspberry Pi and crontab

Based on https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4

First of all, run
`sudo apt-get update`

You should also run `sudo apt-get upgrade`, but it might take quite a while. Skip if in a hurry and run it later.

Then run
`sudo apt-get install python-dev python-dev git`
to install needed libraries.

Then install the (Adafruit Python DHT library)[https://github.com/adafruit/Adafruit_Python_DHT]:
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
cd Adafruit_Python_DHT 
sudo python setup.py install`

You'll need a ThingSpeak channel, so (go create one)[http://thingspeak.com].
Name your channel whatever you like.
Field 1 is for temperature, so name apropriately.
Field 2 is for humidity, so name apropriately.
Remember that there's no need for a timestamp channel, as it is recorded in each «field»

Then there's time to install this simple snippet of code.

`git clone https://github.com/fmandal/dht22.git`

Update with your API key and pin number for the DHT22:

`cd dht22
nano dht22.py`

Change the config variables to reflect your values:
`myAPI = "<API FROM THINGSPEAK>"
pin = 4`

If you'd like it to run every 5 minutes do so via crontab:
`crontab -e 
*/5 * * * * python /home/pi/dht22/dht22.py > /dev/null`
