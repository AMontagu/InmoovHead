from channels.routing import route, include, route_class
from test2.consumers import ws_add, ws_message, ws_disconnect, TtsJsonConsumer

apiSocket = [
	route_class(TtsJsonConsumer, path=r"^/tts/"),
	route_class(TtsJsonConsumer, path=r"^/movement/"),
	route("websocket.connect", ws_add),  # default for getting connection not in hease protocol remove in release
	route("websocket.receive", ws_message),  # default for getting message not in hease protocol remove in release
	route("websocket.disconnect", ws_disconnect),
	# default for getting disconnection not in hease protocol remove in release
]

channel_routing = [
	include(apiSocket, path=r'^/ws')
]
