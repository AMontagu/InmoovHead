import os

import pygame as pg
from gtts import gTTS

counter = 1

class Tts:

	tts_file = ""
	text = ""
	lang = ""

	def __init__(self, tts_file, text, lang):
		self.tts_file = tts_file
		self.text = text
		self.lang = lang

		freq = 24000
		bitsize = -16
		channels = 2
		buffer = 4096
		pg.mixer.init(freq, bitsize, channels, buffer)

	def createAndPlay(self, volume):
		tts = gTTS(self.text, self.lang)
		global counter
		tts.save("testSpeech/sounds/" + self.tts_file+str(counter)+str(".mp3"))

		pg.mixer.music.set_volume(volume)
		clock = pg.time.Clock()
		try:
			pg.mixer.music.load("testSpeech/sounds/" + self.tts_file + str(counter) + str(".mp3"))
			print("Music file {} loaded!".format(self.tts_file + str(counter) + str(".mp3")))
		except pg.error:
			print("File {} not found! ({})".format(self.tts_file + str(counter) + str(".mp3"), pg.get_error()))
			return
		pg.mixer.music.play()
		while pg.mixer.music.get_busy():
			clock.tick(100)
		pg.mixer.music.stop()
		pg.mixer.quit()

		counter += 1


