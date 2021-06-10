import socket, pickle, struct

class videosocket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, host, port):
		self.sock.connect((host, port))

	def videosend(self, frame):
		a = pickle.dumps(frame)
		message = struct.pack("Q",len(a))+a
		self.sock.sendall(message)

	def videoreceive(self):
		data = b""
		payload_size = struct.calcsize("Q")
		while True:
			while len(data) < payload_size:
				packet = self.sock.recv(4*1024) # 4K
				if not packet: break
				data+=packet
			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q",packed_msg_size)[0]

			while len(data) < msg_size:
				data += self.sock.recv(4*1024)
			frame_data = data[:msg_size]
			data  = data[msg_size:]
			frame = pickle.loads(frame_data)
   