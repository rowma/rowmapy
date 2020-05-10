from rowmapy import Rowma
import json

rowma = Rowma()

conn_list = rowma.get_current_connection_list()
# Connect to the first robot in the official public network
robot = rowma.get_robot_status(conn_list[0]['uuid'])
rowma.connect()
print('robot: '+robot['uuid'])
print('application: '+rowma.uuid)

rowma.set_topic_route(robot['uuid'], 'application', rowma.uuid, '/chatter')

def on_chatter(msg):
    print('sample.py'+json.dumps(msg))

rowma.subscribe('/chatter', on_chatter)
