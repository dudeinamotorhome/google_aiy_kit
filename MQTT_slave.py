#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time

# This is the Publisher
zz = ""
s_id = "S1"
flag = 0 
# Connecto to MQTT Server
def on_connect(client, userdata, flags, rc):
	global flag
	print("Connected with result code " + str(rc))
	if rc == 0:
		flag = 1
		client.subscribe('/Text')
		client.subscribe('/Response')
		print("Connected")	
		client.publish('/Text',"Hi.")
		# client.publish('/status',s_id+"/1")

	
def on_message(client, userdata, msg):
	global zz
	if msg.topic == "/Text":
		pass
		# zz = msg.payload
		# print zz
		# client.publish('/Response',"How are you?")
		
	if msg.topic == "/Response":
		print ("Response msg- " , msg.payload)
		

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


def main():
	global zz
	while flag == 0:
		try:
			client.connect("127.0.0.1", 1883)
			client.loop_start()
			time.sleep(3)
		except:
			print("MQTT server connect error")

	#for i in range (0,100):
	#	client.publish("/norin",str(i))
	#	time.sleep(1)
	while(True):
		pass




if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
