
from ipaddress import ip_address
from time import sleep
from time import *
import os
import time
import datetime
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import logging
import paho.mqtt.client as paho
import argparse

#parser = argparse.ArgumentParser(description='function for postgresql')
#parser.add_argument('--ip',default = 'localhost', metavar='', help ='ip x of database server')
#parser.add_argument('--pw',metavar='',default = 'sselab0812!', help ='password for database')
#args = parser.parse_args()

## global ip_address, password
#ip_address = args.ip
#password = args.pw
ip_address = '203.255.56.50'
password = 'sselab0812!'





# mqtt tools
def initialize_key(ACCESS_TOKEN):
    broker='localhost'
    port=1883 

    def on_publish(client,userdata,result):
        print(f"{ACCESS_TOKEN} - Has been connected successfully \n")
        pass
    timestamp = datetime.datetime.now() - datetime.timedelta(days=2)
    print(timestamp)
    timestamp = int(datetime.datetime.timestamp(timestamp)*1000)
    print(timestamp)
    value = 10
    
    # a = {}
    key = input("key:")
    value = input("value:")
    # a[key]=value
    

    msg = {"ts" : timestamp,"values":{key: value}}
    # msg = "{'test':" +str(a)+"}"
    
    print(msg)
    
    command = f'mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "{ACCESS_TOKEN}" -m {msg}' # without timestamp
    command = f'mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u {ACCESS_TOKEN} -m "{msg}"' # with timestamp
    
#    mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "MC2uDxjFJCGDJz6RLx3n" -m {"temperature":25}
    print(command)
    os.system(command)


token = '"d7jKtipCYLguxpAwMa7W"'
initialize_key(token)
