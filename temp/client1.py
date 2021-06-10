import socket, videosocket
from videofeed import VideoFeed

class Client:
	def __init__(self, ip = '127.0.0.1'):
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((ip, 9999))
		self.vsock = videosocket.videosocket(self.client_socket)
		self.videofeed = VideoFeed(1, "client", 1)

	def connect(self):
		while True:
			frame = self.videofeed.get_frame()
			self.vsock.videosend(frame)
			frame = self.vsock.videoreceive()
			self.videofeed.set_frame(frame)

if __name__ == "__main__":
	ip = '127.0.0.1'
	print("Connecting to ",ip," ...")
	client = Client(ip)
	client.connect()