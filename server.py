import cv2
import dlib
import numpy as np
import socket, pickle, struct

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
#host_ip = socket.gethostbyname(host_name)
host_ip = '127.0.0.1'
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    # Load the detector
    detector = dlib.get_frontal_face_detector()

    # Load the predictor
    predictor = dlib.shape_predictor("C://Users//Gaurav//Downloads//shape_predictor_81_face_landmarks.dat")

    if client_socket:
        cap = cv2.VideoCapture(0)
        i=0
        
        while(cap.isOpened()):
            _, frame = cap.read()
            #choose any path u want to here
            path = 'C:\\imgs\\img'+str(i)+'.jpg'
            cv2.imwrite(path,frame)
            i = i+1
            # Convert image into grayscale
            gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        
            black = np.zeros((gray.shape[0],gray.shape[1],3), np.uint8)
        
            # Use detector to find landmarks
            faces = detector(gray)
        
            for face in faces:
                x1 = face.left()  # left point
                y1 = face.top()  # top point
                x2 = face.right()  # right point
                y2 = face.bottom()  # bottom point
        
                # Create landmark object
                landmarks = predictor(image=gray, box=face)
        
        
                # Loop through all the points
                for n in range(0, 81):
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y
        
                    # Draw a circle
                    cv2.circle(img=black, center=(x, y), radius=1, color=(0, 255,0),thickness=-1)
            
            a = pickle.dumps(black)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO',black)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()
                break # When everything done, release the video capture and video write objects
    cap.release() #inside if
                
                # Close all windows
    cv2.destroyAllWindows() #inside if