import socketio
import uuid
import json
import requests

class Rowma:
    def __init__(self, base_url):
        self.base_url = base_url
        self.sio = socketio.Client()
        self.uuid = str(uuid.uuid4())
        self.namespace = '/rowma'

    def connect(self):
        self.sio.connect(self.base_url, namespaces=[self.namespace])
        payload = { 'deviceUuid': self.uuid }
        self.sio.emit('register_device', data=payload, namespace=self.namespace)

    def run_launch(self, uuid, command):
        destination = { 'type': 'robot', 'uuid': uuid }
        payload = { 'destination': destination, 'command': command }
        self.sio.emit('run_launch', data=payload, namespace=self.namespace)

    def publish_topic(self, uuid, msg):
        destination = { 'type': 'robot', 'uuid': uuid }
        payload = { 'destination': destination, 'msg': msg }
        self.sio.emit('delegate', payload)

    def subscribe_topic(self, dest_type, dest_uuid, topic_dest_uuid, topic):
        destination = { 'type': dest_type, 'uuid': dest_uuid }
        topic_destination = { type: 'robot', uuid: topic_dest_uuid }
        msg = {
          'op': 'subscribe',
          'topicDestination': topic_destination,
          'topic': topic
        }
        payload = {
                'destination': destination,
                'msg': msg
                }
        self.sio.emit('delegate', payload)

    def run_rosrun(self, uuid, command, args=''):
        destination = { 'type': 'robot', 'uuid': uuid }
        payload = {
                'destination': destination,
                'command': command,
                'args': args
                }
        self.sio.emit('run_rosrun', payload)

    def kill_nodes(self, uuid, rosnodes):
        destination = { 'type': 'robot', 'uuid': uuid }
        payload = {
                'destination': destination,
                'command': command,
                'args': args
                }
        self.sio.emit('run_rosrun', payload)

    # TODO: Error handling
    def get_current_connection_list(self):
        r = requests.get(self.base_url + '/list_connections')
        return json.loads(r.text)

    # TODO: Error handling
    def get_robot_status(self, uuid):
        params = { 'uuid': uuid }
        r = requests.get(self.base_url + '/robots', params=params)
        return json.loads(r)
