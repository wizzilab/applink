#!/usr/bin/python3

from paho.mqtt import client as mqtt_client
import json
import uuid
import argparse
import arg_parsing


# =================================================================================
# Parameter parsing
# ================================================================================= 
parser = argparse.ArgumentParser(description="Read example")
arg_parsing.add_connection_parameters(parser)
arg_parsing.add_read_parameters(parser)
args = parser.parse_args()

broker = args.host
port = args.port
companyID = args.company_id
username = args.username
password = args.password
cid = args.id

topic = "/applink/" + companyID + "/remotectrl"
client_id = username + ":" + str(cid)

# =================================================================================
# Function to connect to the MQTT queue
# ================================================================================= 
def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.tls_set()
    client.connect(broker, port)
    return client

# =================================================================================
# Function to subscribe to a topic
# ================================================================================= 
def subscribe(client, topic):
    def on_message(client, userdata, msg):
        msg_str = msg.payload.decode()
        print(f"Received `{msg_str}` from `{msg.topic}` topic")
        msg = json.loads(msg_str)
        print("Meta data : " + str(msg["meta"]))
        client.disconnect()

    client.subscribe(topic)
    client.on_message = on_message

# =================================================================================
# Function to post a message in a topic
# =================================================================================
def publish(client, msg, topic):
    status = 1
    result = client.publish(topic, msg)
    result.wait_for_publish()
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


# =================================================================================
# Function to make a read request via the mqtt queue
# =================================================================================
def read_example(client, uid, fid, field_name):
    msg = {
        "action": "R",
        "user_type": "root",
        "gmuid": "auto",
        "uid": uid,
        "fid": fid,
        "field_name": field_name,
    }
    id = uuid.uuid1()
    subscribe(client, topic + "/response/" + str(id.int))
    publish(client, json.dumps(msg), topic + "/request/" + str(id.int))

# =================================================================================
# Main
# =================================================================================
if __name__ == "__main__":
    client = connect_mqtt()

    uid = args.uid 
    fid = args.fid 
    field_name = args.field 

    read_example(client, uid, fid, field_name)
    client.loop_forever()
