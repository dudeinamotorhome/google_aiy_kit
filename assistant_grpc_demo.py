#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import logging
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import requests
import aiy.i18n
#import MQTT_master
#import MQTT_slave

import paho.mqtt.client as mqtt
import time
import requests

zz = ""
flag = 0
global text
text=""

def on_connect(client, userdata, flags, rc):
	global flag
	global text
	#text=str(text)
        #print(type(text))
        #m=str(text)
	#print(m)
	#text=""+text
	#print(type(text))
	#print("Connected with result code " + str(rc))
	if rc == 0:
		flag = 1
		client.subscribe('/Text')
		client.subscribe('/Response')
		#print("Connected")
		print(text)
		#client.publish('/Text',text)
		client.publish('/Text',text)
    		# client.publish('/status',s_id+"/1")
		#print("message is "+text)

	
def on_message(client, userdata, msg):
	global zz
	#global flag
	if msg.topic == "/Text":
		pass
		# zz = msg.payload
		# print zz
		# client.publish('/Response',"How are you?")
		
	if msg.topic == "/Response":
		b=str(msg.payload)
		print ("Response msg-" , b)
		aiy.audio.say(b)
		if b=="Bye":
                    aiy.audio.say("Bye")
                    client.loop_stop()
		
		#flag=0
		
def on_disconnect(client,userdata,rc=0):
    #logging.debug("Disconnected result code "+str(rc))
    client.loop_stop()
    
#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_disconnect=on_disconnect
def publish_msg():
    client.publish('/Text',text)
    
def agriculture():
    #URL="https://dag.infinium.management/GIS_GUJ/agrigis/getalexa"
    URL="http://27.109.18.94:8080/Agriculture_GIS_Geomation/agrigis/getalexa"
    PRAMAS=text
    r=requests.get(url=URL,params={'param':PRAMAS})
    #aiy.audio.say(r.text,lang="fr-FR")
    aiy.audio.say(r.text)
    print(r.status_code)
    print(r.text)
    #print(r.encode)
    

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

talukas=['sweet','hi','home','traffic','Gujarat','gujarat','ahmedabad','bavla','daskroi','detroj-rampura','dhandhuka','dholera','dholka','mandal','sanand','viramgam']
def main():
    global text
    #print("hello")
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    aiy.i18n.set_language_code('en-GB')
    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            #global text
            #text=assistant.recognize()
            text, audio = assistant.recognize()
            #print(type(text))
            #print(text)
            f=0
            #flag=0
            if text:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                #elif text=='hello':
                #    print('hi')
                #    break;
                #print('You said "', text, '"')
                #b="mehsana"
                #aiy.audio.say(b)
            #if flag==1:
                #publish_msg()
                #get(text)
                #for item in talukas:
                    #print(item)
                #for item in talukas:
                 #   if item  in text:
                  #      f=1
                   #     print("word has been recognized by api")
                    #    break
                #if f==0:
                 #   print("pronounce correctly")
                
            #print("hello")
            #b="master"
            #print(b)
               # aiy.audio.say(b)
                #res=aiy.audio.record_to_wave(text)
                #play_wave(res)
            #global zz
                #print(zz)
            #print(flag)
            agriculture()
            #while flag == 0:
             #   try:
                    #print("try to connect")
                        #print(text)
              #      client.connect("127.0.0.1", 1883)
              #      client.loop_start()
               #     time.sleep(3)
                #except:
                #    print("MQTT server connect error")
                
            #if audio:
                #aiy.audio.play_audio(audio)
def get(text):
    print(text)
    return text


main()
