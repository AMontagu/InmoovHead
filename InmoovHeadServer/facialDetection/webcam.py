if __name__ == "__main__":
	main = True
else:
	main = False

import threading
import cv2
import numpy
import os

if not main:
	from testSpeech.Tts import Tts
	from headServer.settings import BASE_DIR

class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class FacialDetection(threading.Thread, metaclass=Singleton):
	def __init__(self):
		super(FacialDetection, self).__init__()
		print("IJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHKG")

		if not main:
			cascPath = os.path.join(BASE_DIR, "facialDetection", "haarcascade_frontalface_default.xml")
		else:
			cascPath = "haarcascade_frontalface_default.xml"
		self.faceCascade = cv2.CascadeClassifier(cascPath)

		self.video_capture = cv2.VideoCapture(0)
		self.time = 0
		self.total = 0
		self.countTable = []

		self.running = True

	def run(self):
		while self.running:
			# Capture frame-by-frame
			ret, frame = self.video_capture.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			count = 0

			faces = self.faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags=cv2.CASCADE_SCALE_IMAGE
			)

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
				count += 1
			self.countTable.append(count)

			# Display the resulting frame
			#cv2.imshow('Video', frame)

			print('count : ' + str(count))
			#print(self.time)
			self.total += count
			self.time += 1
			#print('time :'+ str(self.time))
			#if self.time > 60:
				#print('total :'+ str(self.total))
				#break

			'''if main == False:
				if self.total > 0 and self.time > 500:
					numberFace = int(numpy.around(self.total / self.time))
					if numberFace == 0 :
						numberFace = "une"
					tts = Tts("tts.mp3", "Bonjour je detecte" + str(numberFace) + 'personne', "fr")
					tts.createAndPlay(0.7)
					self.total = 0
					self.time = 0'''
			if main == False:
				if self.countTable.count(1) > 0 and self.time > 120 :
					#if self.countTable.count(0) > 0:
						#self.countTable.remove(0)
					#on parcours la table qui a permis de stocker le nombre de visage trouver durant les 120 frame
					i = 1
					while self.countTable.count(i) > 0 :
						i += 1
					facesPourcent = self.countTable.count(i) / len(self.countTable)
					if facesPourcent < 0.2:
						#comme on est en dessous des 20% on passe au nombre de visage en dessous jusqu'à etre au dessu du taux demandé
						while facesPourcent < 0.2:
							i -= 1
							facesPourcent = self.countTable.count(i) / len(self.countTable)
							print(facesPourcent, self.countTable.count(i), len(self.countTable))
					numberFace = i
					if i == 1:
						numberFace = 'une'
					if i > 0:
						tts = Tts("tts", "Bonjour je detecte" + str(numberFace) + 'personne', "fr")
						tts.createAndPlay(0.7)
					self.time = 0
					self.countTable = []

			if cv2.waitKey(1) & 0xFF == ord('q'):
				print(self.countTable.count(1))
				print(self.countTable.count(2))
				print(self.countTable)
				break



		self.video_capture.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	facialDetection = FacialDetection()
	facialDetection.start()
