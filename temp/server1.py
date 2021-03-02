import socket, videosocket
from videofeed import VideoFeed

class Server:
	def __init__(self):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind(("", 9999))
		self.server_socket.listen(5)
		self.videofeed = VideoFeed(1, "server", 1)
		print("TCP server waiting for client on port 9999")

	def start(self):
		while True:
			client_socket, address = self.server_socket.accept()
			print("Got a connection from", address)
			vsock = videosocket.videosocket(client_socket)
			while True:
				frame = vsock.videoreceive()
				self.videofeed.set_frame(frame)
				frame = self.videofeed.get_frame()
				vsock.videosend(frame)

if __name__ == "__main__":
	server = Server()
	server.start()