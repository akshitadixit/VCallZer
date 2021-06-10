import cv2
import dlib
import numpy as np
import socket, pickle, struct

# Load the detector
detector = dlib.get_frontal_face_detector()
# Load the predictor
predictor = dlib.shape_predictor("C:\\Users\\Gaurav\\Downloads\\shape_predictor_81_face_landmarks.dat")


class VideoFeed:
	def __init__(self, mode=1, name="window1", capture=1):
		print(name)
		self.camera_index = 0
		self.name = name
		if capture == 1:
			self.cam = cv2.VideoCapture(self.camera_index)

	def get_frame(self):
		_, frame = self.cam.read()
		i = 0
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

		k = cv2.waitKey(1)
		if(k=='q'):
			self.camera_index += 1 #try the next camera index
			self.cam = cv2.VideoCapture(self.camera_index)
			if not self.cam: #if the next camera index didn't work, reset to 0.
				self.camera_index = 0
				self.cam = cv2.VideoCapture(self.camera_index)
		
		return black

	def set_frame(self, frame):
		cv2.imshow(self.name, frame)