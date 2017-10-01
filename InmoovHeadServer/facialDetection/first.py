import cv2
import numpy
from testSpeech.Tts import Tts

cascPath = eval(input())
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
time = 0
total = 0
while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	count = 0
	faces = faceCascade.detectMultiScale(
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
	print(time)
	total += count
	time += 1
	print(time)
	if time > 60:
		print(total)
		break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
if total > 0:
	numberFace = total / (time - 1)
	welcomeX = numpy.around(numberFace, 1)
	print(numpy.around(numberFace, 1))
	for i in range(0, int(numberFace)):
		# welcome = "Bonjour monsieur"
		tts = Tts.Tts("tts.mp3", "Bonjour monsieur" + str(i), "fr")
		tts.createSpeech()
		tts.play_music(0.7)
		print("Bonjour monsieur " + str(i))
video_capture.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
	from TTS import Tts
