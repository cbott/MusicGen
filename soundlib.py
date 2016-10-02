
import math
import pyaudio
import random

class TonePlayer():
	def __init__(self, bitrate=16000):
		self.bitrate = bitrate
		self.player = pyaudio.PyAudio()
		self.stream = self.player.open(format = self.player.get_format_from_width(1), 
             	   			channels = 1, 
                			rate = self.bitrate, 
                			output = True)

	def wave_progression(self, pos, freq):
		return math.sin( pos / ((self.bitrate/freq) / math.pi) )

	def add_tone(self, freq, sec):
		segment = ''
		for frame in xrange(int(self.bitrate*sec)):
			segment+=chr(int(self.wave_progression(frame,freq)*127+128))
		return segment

	def play(self, freqs, time=1):
		"""Play a list of frequencies"""
		song = ''
		for f in freqs:
			song += self.add_tone(f, time)

		self.stream.start_stream()
		self.stream.write(song)
		self.stream.stop_stream()

#stream.close()
#p.terminate()
