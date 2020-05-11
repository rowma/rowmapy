from rowmapy import Rowma
import json

rowma = Rowma()

conn_list = rowma.get_current_connection_list()
# Get the first robot in the official public network
robot = conn_list[0]
rowma.connect()
print('robot: '+robot['uuid'])
print('application: '+rowma.uuid)

rowma.set_topic_route(robot['uuid'], 'application', rowma.uuid, '/chatter')

def on_chatter(msg):
    print(msg)

rowma.subscribe('/chatter', on_chatter)
rowma.publish(robot['uuid'], '/chatter', { "data": "topic from python" })
