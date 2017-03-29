from django.apps import AppConfig
import os
from headServer.settings import BASE_DIR

class Test2Config(AppConfig):
	name = 'test2'

	def ready(self):
		soundDirName = os.path.join("testSpeech", "sounds")
		dirSound = os.path.join(BASE_DIR, soundDirName)
		for f in os.listdir(dirSound):
			os.remove(os.path.join(dirSound, f))
