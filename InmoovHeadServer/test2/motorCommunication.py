import threading
import time
import serial
import sys
import glob
from headServer.settings import LINUX, ARDUINOPLUG


class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


class SerialCom(threading.Thread):
	def __init__(self, port='COM3', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS):
		if LINUX:
			port = 'tty0'
		print("created")
		super(SerialCom, self).__init__(daemon=True)
		self.running = True
		self.open = False
		self.available = False
		availablePort = self.serial_ports()
		print(availablePort)
		if ARDUINOPLUG:
			if LINUX:
				for p in availablePort:
					if p.startswith('/dev/tty') and p != '/dev/ttyAMA0':
						print("start with good start")
						self.available = True
			else:
				if len(availablePort) > 0:
					self.available = True
		else:
			print("ici")
			self.available = False
		if self.available:
			try:
				self.ser = serial.Serial(
					port=port,
					baudrate=baudrate,
					parity=parity,
					stopbits=stopbits,
					bytesize=bytesize
				)
				"""parity=parity,
					stopbits=stopbits,
					bytesize=bytesize"""
				#self.ser.write("testOpen")
			except IOError as e:
				print(e)

		else:
			print("no arduino available")
			self.ser = None

	def run(self):
		while self.running:
			if self.available:
				self.open = self.initSerial()

				try:
					while self.open:
						input = self.ser.readline()
						if(input != ""):
							print(bytes.decode(input))
				except IOError:
					pass
				self.closeSerial()
			else:
				#TODO CHECK IF NEW ARDUINO CARD PLUGGED IN EVERY 3 SECONDS SOR SOMETHING LIKE THAT
				self.running = False

	def write(self, data):
		if self.open:
			#maybe need ths line:
			#self.ser.write(data + '\r\n')
			print("send this : " + str(data))
			self.ser.write(data)
			#self.ser.write(str(data))

	def initSerial(self):
		if self.available:
			self.ser.open()
			self.open = True
		return self.open

	def closeSerial(self):
		if self.available:
			self.open = False
			self.running = False
			self.ser.close()

	def serial_ports(self):
		""" Lists serial port names

			:raises EnvironmentError:
				On unsupported or unknown platforms
			:returns:
				A list of the serial ports available on the system
		"""
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			# this excludes your current terminal "/dev/tty"
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')
		else:
			raise EnvironmentError('Unsupported platform')

		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)
			except (OSError, serial.SerialException):
				pass
		return result


class MotorCommunication(SerialCom, metaclass=Singleton):
	def __init__(self, port='COM3', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS):
		super(MotorCommunication, self).__init__(port, baudrate, parity, stopbits, bytesize)

	def sendJson(self, json):
		if not isinstance(json, str):
			json = str(json)
		self.write(bytes(json, "utf-8"))

	def sendMove(self, motorNumber, position):
		json = {"motorNumber": motorNumber, "position": position}


if __name__ == '__main__':
	serialCom = SerialCom()

	serialCom.daemon = True
	serialCom.start()

	while True:
		time.sleep(2)
		""""#print(serialCom.serial_ports())
		#serialCom.write("a" + "\r\n")
		serialCom.write(bytes("a", "utf-8"))
		time.sleep(2)
		#serialCom.write("z" + "\r\n")
		serialCom.write(bytes("z", "utf-8"))"""
		# {"action":"moveHeadRight", "degrees": 10}
		# {"action":"moveHeadUp", "degrees": 20}
		serialCom.write(bytes("{\"action\":\"moveHeadRight\", \"degrees\": 10}", "utf-8"))
		time.sleep(20)
