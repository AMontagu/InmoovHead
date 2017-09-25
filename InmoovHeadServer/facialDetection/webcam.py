if __name__ == "__main__":
	main = True
else:
	main = False

import threading
import cv2
import numpy

if not main:
	from testSpeech.Tts import Tts

class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class FacialDetection(threading.Thread, metaclass=Singleton):
	def __init__(self):
		super(FacialDetection, self).__init__(daemon=True)

		cascPath = eval(input())
		self.faceCascade = cv2.CascadeClassifier(cascPath)

		self.video_capture = cv2.VideoCapture(0)
		self.time = 0
		self.total = 0

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
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
				count += 1

			# Display the resulting frame
			cv2.imshow('Video', frame)

			print('count : ' + str(count))
			print(self.time)
			self.total += count
			self.time += 1
			print(self.time)
			if self.time > 60:
				print(self.total)
				break
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		if not main:
			if self.total > 0:
				numberFace = self.total / (self.time - 1)
				welcomeX = numpy.around(numberFace, 1)
				print(numpy.around(numberFace, 1))
				for i in range(0, int(numberFace)):
					# welcome = "Bonjour monsieur"
					tts = Tts.Tts("tts.mp3", "Bonjour monsieur" + str(i), "fr")
					tts.createSpeech()
					tts.play_music(0.7)
					print("Bonjour monsieur " + str(i))

		self.video_capture.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	facialDetection = FacialDetection()
	facialDetection.start()
