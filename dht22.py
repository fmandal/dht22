""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
Modified again by Fredrik Mandal on June 6, 2017
"""
import sys
import Adafruit_DHT
import urllib2

myAPI = "<API KEY>"
pin = 4

def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
   print "Temp: %s, Hum: %s" % (str(T), str(RH))
   return RH, T

def sendToThingSpeak(RH, T):
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
   callURL = baseURL + "&field1=%s&field2=%s" % (str(T), str(RH))
   f = urllib2.urlopen(callURL)
   res = f.read()
   f.close()
   print res
   return res

def main():
   print "Starting"
   RH = None
   T = None
   sent = "0"
   while RH == None:
      print "Getting sensor data"
      RH, T = getSensorData()
   while sent == "0":
      print "Sending to ThingSpeak"
      sent = sendToThingSpeak(RH, T)
   print "Done\n"

if __name__ == '__main__':
   main()
