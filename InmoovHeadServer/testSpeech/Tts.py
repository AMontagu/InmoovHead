import pygame as pg
from gtts import gTTS

class Tts:

    tts_file = ""
    text = ""
    lang = ""

    def __init__(self, tts_file, text, lang):
        self.tts_file = tts_file
        self.text = text
        self.lang = lang

    def play_music(self,volume=0.8):

        freq = 24000
        bitsize = -16
        channels = 2
        buffer = 4096
        pg.mixer.init(freq, bitsize, channels, buffer)

        pg.mixer.music.set_volume(volume)
        clock = pg.time.Clock()
        try:
            pg.mixer.music.load(self.tts_file)
            print("Music file {} loaded!".format(self.tts_file))
        except pg.error:
            print("File {} not found! ({})".format(self.tts_file, pg.get_error()))
            return
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            clock.tick(100)

    def createSpeech(self):
        tts = gTTS(self.text, self.lang)
        tts.save(self.tts_file)

