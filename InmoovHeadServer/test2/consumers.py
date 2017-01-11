import json

from channels import Group
from channels.generic.websockets import JsonWebsocketConsumer

class TtsJsonConsumer(JsonWebsocketConsumer):
	"""
	Handle the groups of all the robots for broadcasting informations to all the robots

	see https://channels.readthedocs.io/en/latest/generics.html
	"""
	http_user = True
	# Set to True if you want them, else leave out
	strict_ordering = False
	slight_ordering = False

	def connection_groups(self, **kwargs):
		print("connection Chat groups json")
		return ["bla", "bla2"]

	def connect(self, message, **kwargs):
		print("connect Chat json")

	def receive(self, content, **kwargs):
		print("receive Chat json :")
		print(content)

		self.send("bla self")

		Group("bla").send({
			'text': "bla groups"
		})

	def disconnect(self, message, **kwargs):
		print("disconnect Chat json")


def ws_add(message):
	print("add not in hease protocole :")
	print(message.content)
	print(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
	print("disconnect not in hease protocole :")
	print(message.content)


def ws_message(message):
	print("message not in hease protocole :")
	print(message.content)
	print(message.content['text'])