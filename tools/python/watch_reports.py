#!/usr/bin/python3

from paho.mqtt import client as mqtt_client
import json
import argparse
import arg_parsing


# =================================================================================
# Parameter parsing
# ================================================================================= 
parser = argparse.ArgumentParser(description="Watch reports")
arg_parsing.add_connection_parameters(parser)
args = parser.parse_args()

broker = args.host
port = args.port
companyID = args.company_id
username = args.username
password = args.password
cid = args.id

topic = "/applink/" + companyID + "/report/#"
client_id = username + ":" + str(cid)


# =================================================================================
# Function to connect to the MQTT queue
# ================================================================================= 
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT !")
        else:
            print("Failed to connect, error code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set()
    client.connect(broker, port)
    return client


# =================================================================================
# Function to subscribe to the report topic
# ================================================================================= 
def watch_reports(client):
    def on_message(client, userdata, msg):
        msg_str = msg.payload.decode()
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

# =================================================================================
# Main
# =================================================================================
if __name__ == "__main__":
    client = connect_mqtt()
    watch_reports(client)
    client.loop_forever()
