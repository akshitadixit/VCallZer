import socket
import cv2
import pickle
import struct

#creating socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#the below is applicable for local host
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

#binding socket
server_socket.bind(socket_address)

#listening to socket [increase value to 15 incase of valueError]
server_socket.listen(5)
print("Server port:",socket_address)

#accepting client socket connections
while True:
    client_socket,addr = server_socket.accept()
    print('Connected to:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('Video transmission',frame)

	    #press esc to exit
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()