from __future__ import division
import time
# Import the PCA9685 module.
import Adafruit_PCA9685

class motorController:
# TODO: in the future, this could be made smarter eg:
#   - configurable speed/acceleration of the arduino motor controller.
#   - Ack from the arduino to confirm move completion. This would be used to
#       allow the GUI to be smarter (update the current state automatically, etc)

	def __init__(self):
		# Uncomment to enable debug output.
		#import logging
		#logging.basicConfig(level=logging.DEBUG)

		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = Adafruit_PCA9685.PCA9685()

		# Min/max pulse length out of 4096
		self.arm_bot = 120  # Brings servo 1/3 to top position and 5/7 to bottom
		self.arm_mid = 375  # Brings servo 1/3/5/7 to mid positon
		self.arm_top = 670  # Brings servo 5/7 to top position and 1/3 to bottom

		self.arm_out = 400  # Brings slider sechansim in to cube
		self.arm_in = 500 # Brings slider mechanism out away from cube

		# Set frequency to 60hz, good for servos.
		self.pwm.set_pwm_freq(60)

		self.pwm.set_pwm(0, 0, self.arm_out)
		self.pwm.set_pwm(1, 0, self.arm_top)
		#time.sleep(2)
		self.pwm.set_pwm(0, 0, self.arm_in)

		self.pwm.set_pwm(2, 0, self.arm_out)	
		self.pwm.set_pwm(3, 0, self.arm_bot)
		#time.sleep(2)
		self.pwm.set_pwm(2, 0, self.arm_in)
			
		self.pwm.set_pwm(4, 0, self.arm_out)
		self.pwm.set_pwm(5, 0, self.arm_top)
		#time.sleep(2)
		self.pwm.set_pwm(4, 0, self.arm_in)
				
		self.pwm.set_pwm(6, 0, self.arm_out)
		self.pwm.set_pwm(7, 0, self.arm_bot)
		#time.sleep(2)
		self.pwm.set_pwm(6, 0, self.arm_in)

		self.move_arml = self.arm_top
		self.move_armf = self.arm_bot
		self.move_armr = self.arm_top
		self.move_armb = self.arm_bot

		#print('')	
		#print('All arms in up top position')
		#print('')

	def set_servo_pulse(self, channel, pulse):

		# Helper function to make setting a servo pulse width simpler.
		pulse_length = 1000000    # 1,000,000 us per second
		pulse_length //= 60       # 60 Hz
		#print('{0}us per period'.format(pulse_length))
		pulse_length //= 4096     # 12 bits of resolution
		#print('{0}us per bit'.format(pulse_length))
		pulse *= 1000
		pulse //= pulse_length
		self.pwm.set_pwm(channel, 0, pulse)
		
	def read_in_colours(self, move):
		
		self.pwm.set_pwm(0, 0, self.arm_out)
		self.pwm.set_pwm(1, 0, self.arm_bot)
		#time.sleep(1)
		self.pwm.set_pwm(0, 0, self.arm_in)

		self.pwm.set_pwm(2, 0, self.arm_out)	
		self.pwm.set_pwm(3, 0, self.arm_bot)
		#time.sleep(1)
		self.pwm.set_pwm(2, 0, self.arm_in)
			
		self.pwm.set_pwm(4, 0, self.arm_out)
		self.pwm.set_pwm(5, 0, self.arm_top)
		#time.sleep(1)
		self.pwm.set_pwm(4, 0, self.arm_in)
				
		self.pwm.set_pwm(6, 0, self.arm_out)
		self.pwm.set_pwm(7, 0, self.arm_bot)
		#time.sleep(1)
		self.pwm.set_pwm(6, 0, self.arm_in)
		
		#print('All arms in top position')
		#print('')
		#time.sleep(2)
				
		if move == "X":

			self.pwm.set_pwm(0, 0, self.arm_out)
			self.pwm.set_pwm(4, 0, self.arm_out)
			self.pwm.set_pwm(1, 0, self.arm_top)
			self.pwm.set_pwm(5, 0, self.arm_bot)
			#print('Left and right arms out, left and right arms in top position')
			#time.sleep(2)

			self.pwm.set_pwm(1, 0, self.arm_mid)
			self.pwm.set_pwm(5, 0, self.arm_mid)
			#print('Cube ')
			#time.sleep(2)
			
			#print('Read face')
			#print('')
			#time.sleep(2)
			
		elif move == "X'":
			
			self.pwm.set_pwm(0, 0, self.arm_in)
			self.pwm.set_pwm(4, 0, self.arm_in)
			#print('Left and right arms-in')
			#time.sleep(2)

			self.pwm.set_pwm(1, 0, self.arm_mid)
			self.pwm.set_pwm(5, 0, self.arm_mid)
			#print('Cube rotates forwards')
			#time.sleep(2)
			
			#print('Read face')
			#print('')
			#time.sleep(2)

		elif move == "Z":
			
			self.pwm.set_pwm(6, 0, self.arm_out)
			self.pwm.set_pwm(7, 0, self.arm_top)
			#print('Back arm out, back arm in top position')
			#time.sleep(2)

			self.pwm.set_pwm(6, 0, self.arm_in)
			#print('Back arm in')
			#time.sleep(2)

			
			self.pwm.set_pwm(3, 0, self.arm_mid)
			self.pwm.set_pwm(7, 0, self.arm_mid)
			#print('Cube rotates to the right')
			#time.sleep(2)
			
			#print('Read face')
			#print('')
			#time.sleep(2)
			
		elif move == "Z'":
			
			self.pwm.set_pwm(2, 0, self.arm_out)
			self.pwm.set_pwm(3, 0, self.arm_top)
			#print('Front arm out, front arm in top position')
			#time.sleep(2)

			self.pwm.set_pwm(2, 0, self.arm_in)
			#print('Front arm-in')
			#time.sleep(2)

			self.pwm.set_pwm(3, 0, self.arm_mid)
			self.pwm.set_pwm(7, 0, self.arm_mid)
			#print('Cube rotates to the left')
			#time.sleep(2)
			
			#print('Read face')
			#print('')
			#time.sleep(2)
				
	def turn_front(self, move):
			
		if move == "F":
		
			if self.move_armf == self.arm_top:
		
				self.pwm.set_pwm(2, 0, self.arm_out)
				self.pwm.set_pwm(3, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(2, 0, self.arm_in)

				#time.sleep(1)

				self.pwm.set_pwm(3, 0, self.arm_mid)
				self.move_armf = self.arm_mid
				
			elif self.move_armf == self.arm_bot:
		
				self.pwm.set_pwm(3, 0, self.arm_mid)
				self.move_armf = self.arm_mid
			
			elif self.move_armf == self.arm_mid:
		
				
				self.pwm.set_pwm(3, 0, self.arm_top)
				self.move_armf = self.arm_top
			
			#print('Front face turned c/w')
			#print('')

		elif move == "F'":
				
			if self.move_armf == self.arm_bot:
				
				self.pwm.set_pwm(2, 0, self.arm_out)
				self.pwm.set_pwm(3, 0, self.arm_top)
				#time.sleep(2)
				self.pwm.set_pwm(2, 0, self.arm_in)
				#time.sleep(1)
				self.pwm.set_pwm(3, 0, self.arm_mid)
				self.move_armf = self.arm_mid
				
			elif self.move_armf == self.arm_top:
			
				self.pwm.set_pwm(3, 0, self.arm_mid)
				self.move_armf = self.arm_mid
			
			elif self.move_armf == self.arm_mid:
				
				self.pwm.set_pwm(3, 0, self.arm_bot)
				self.move_armf = self.arm_bot		
			
			#print('Front face turned ac/w')
			#print('')

		elif move == "F2":
		
			if self.move_armf == self.arm_mid:
				
				self.pwm.set_pwm(2, 0, self.arm_out)
				self.pwm.set_pwm(3, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(2, 0, self.arm_in)

				#time.sleep(1)

				self.pwm.set_pwm(3, 0, self.arm_top)
				self.move_armf = self.arm_top
				
			elif self.move_armf == self.arm_bot:
			
				self.pwm.set_pwm(3, 0, self.arm_top)
				self.move_armf = self.arm_top
			
			elif self.move_armf == self.arm_top:
			
				self.pwm.set_pwm(3, 0, self.arm_bot)
				self.move_armf = self.arm_bot
			
			#print('Front face turned twice')
			#print('')

	def turn_right(self, move):

		if move == "R":
		
			if self.move_armr == self.arm_top:
							
				self.pwm.set_pwm(5, 0, self.arm_mid)
				self.move_armr = self.arm_mid
				
			elif self.move_armr == self.arm_bot:

				self.pwm.set_pwm(4, 0, self.arm_out)
				self.pwm.set_pwm(5, 0, self.arm_top)

				#time.sleep(2)

				self.pwm.set_pwm(4, 0, self.arm_in)

				#time.sleep(1)
				self.pwm.set_pwm(5, 0, self.arm_mid)
				self.move_armr = self.arm_mid
			
			elif self.move_armr == self.arm_mid:

				self.pwm.set_pwm(5, 0, self.arm_bot)
				self.move_armr = self.arm_bot
			
			#print('Right face turned c/w')
			#print('')

		elif move == "R'":
				
			if self.move_armr == self.arm_bot:
				
				self.pwm.set_pwm(5, 0, self.arm_mid)
				self.move_armr = self.arm_mid
				
			elif self.move_armr == self.arm_top:
				
				self.pwm.set_pwm(4, 0, self.arm_out)
				self.pwm.set_pwm(5, 0, self.arm_bot)
				#time.sleep(2)
				self.pwm.set_pwm(4, 0, self.arm_in)
				#time.sleep(1)
				
				self.pwm.set_pwm(5, 0, self.arm_mid)
				self.move_armr = self.arm_mid
			
			elif self.move_armr == self.arm_mid:
				
				self.pwm.set_pwm(5, 0, self.arm_top)
				self.move_armr = self.arm_top		
			
			#print('Right face turned ac/w')
			#print('')

		elif move == "R2":
		
			if self.move_armr == self.arm_mid:
				
				self.pwm.set_pwm(4, 0, self.arm_out)
				self.pwm.set_pwm(5, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(4, 0, self.arm_in)

				#time.sleep(1)

				self.pwm.set_pwm(5, 0, self.arm_top)
				self.move_armr = self.arm_top
				
			elif self.move_armr == self.arm_bot:
			
				self.pwm.set_pwm(5, 0, self.arm_top)
				self.move_armr = self.arm_top
			
			elif self.move_armr == self.arm_top:
			
				self.pwm.set_pwm(5, 0, self.arm_bot)
				self.move_armr = self.arm_bot
			
			#print('Right face turned twice')
			#print('')

	def turn_left(self, move):

		if move == "L":
		
			if self.move_arml == self.arm_bot:
							
				self.pwm.set_pwm(1, 0, self.arm_mid)
				self.move_arml = self.arm_mid
				
			elif self.move_arml == self.arm_top:

				self.pwm.set_pwm(0, 0, self.arm_out)
				self.pwm.set_pwm(1, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(0, 0, self.arm_in)

				#time.sleep(1)
				self.pwm.set_pwm(1, 0, self.arm_mid)
				self.move_arml = self.arm_mid
			
			elif self.move_arml == self.arm_mid:

				self.pwm.set_pwm(1, 0, self.arm_top)
				self.move_arml = self.arm_top
			
			#print('Left face turned c/w')
			#print('')

		elif move == "L'":
				
			if self.move_arml == self.arm_top:
				
				self.pwm.set_pwm(1, 0, self.arm_mid)
				self.move_arml = self.arm_mid
				
			elif self.move_arml == self.arm_bot:
				
				self.pwm.set_pwm(0, 0, self.arm_out)
				self.pwm.set_pwm(1, 0, self.arm_top)
				#time.sleep(2)
				self.pwm.set_pwm(0, 0, self.arm_in)
				#time.sleep(1)
				
				self.pwm.set_pwm(1, 0, self.arm_mid)
				self.move_arml = self.arm_mid
			
			elif self.move_arml == self.arm_mid:
				
				self.pwm.set_pwm(1, 0, self.arm_bot)
				self.move_arml = self.arm_bot		
			
			#print('Left face turned ac/w')
			#print('')

		elif move == "L2":
		
			if self.move_arml == self.arm_mid:
				
				self.pwm.set_pwm(0, 0, self.arm_out)
				self.pwm.set_pwm(1, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(0, 0, self.arm_in)

				#time.sleep(1)

				self.pwm.set_pwm(1, 0, self.arm_top)
				self.move_arml = self.arm_top
				
			elif self.move_arml == self.arm_bot:
			
				self.pwm.set_pwm(1, 0, self.arm_top)
				self.move_arml = self.arm_top
			
			elif self.move_arml == self.arm_top:
			
				self.pwm.set_pwm(1, 0, self.arm_bot)
				self.move_arml = self.arm_bot
			
			#print('Left face turned twice')
			#print('')

	def turn_back(self, move):

		if move == "B":
		
			if self.move_armb == self.arm_bot:
							
				self.pwm.set_pwm(7, 0, self.arm_mid)
				self.move_armb = self.arm_mid
				
			elif self.move_armb == self.arm_top:

				self.pwm.set_pwm(6, 0, self.arm_out)
				self.pwm.set_pwm(7, 0, self.arm_bot)

				#time.sleep(2)

				self.pwm.set_pwm(6, 0, self.arm_in)

				#time.sleep(1)
				self.pwm.set_pwm(7, 0, self.arm_mid)
				self.move_armb = self.arm_mid
			
			elif self.move_armb == self.arm_mid:

				self.pwm.set_pwm(7, 0, self.arm_top)
				self.move_armb = self.arm_top
			
			#print('Back face turned c/w')
			#print('')

		elif move == "B'":
				
			if self.move_armb == self.arm_top:
				
				self.pwm.set_pwm(7, 0, self.arm_mid)
				self.move_armb = self.arm_mid
				
			elif self.move_armb == self.arm_bot:
				
				self.pwm.set_pwm(6, 0, self.arm_out)
				self.pwm.set_pwm(7, 0, self.arm_top)
				#time.sleep(2)
				self.pwm.set_pwm(6, 0, self.arm_in)
				#time.sleep(1)
				
				self.pwm.set_pwm(7, 0, self.arm_mid)
				self.move_armb = self.arm_mid
			
			elif self.move_armb == self.arm_mid:
				
				self.pwm.set_pwm(7, 0, self.arm_bot)
				self.move_armb = self.arm_bot		
			
			#print('Back face turned ac/w')
			#print('')

		elif move == "B2":
		
			if self.move_armb == self.arm_mid:
				
				self.pwm.set_pwm(6, 0, self.arm_out)
				self.pwm.set_pwm(7, 0, self.arm_bot)

				#time.sleep(1)

				self.pwm.set_pwm(6, 0, self.arm_in)
				self.pwm.set_pwm(7, 0, self.arm_top)
				self.move_armb = self.arm_top
				
			elif self.move_armb == self.arm_bot:
			
				self.pwm.set_pwm(7, 0, self.arm_top)
				self.move_armb = self.arm_top
			
			elif self.move_armb == self.arm_top:
			
				self.pwm.set_pwm(7, 0, self.arm_bot)
				self.move_armb = self.arm_bot
			
			#print('Back face turned twice')
			#print('')

	def MotorControlString(self, motion):
	
		array = motion.split(' ')
		
		for move in array:
			
			if move == "F" or "F'" or "F2":
		
				self.turn_front(move)

			if move == "R" or "R'" or "R2":
					
				self.turn_right(move)

			if move == "L" or "L'" or "L2":
			
				self.turn_left(move)

			if move == "B" or "B'" or "B2":
			
				self.turn_back(move)

			if move == "U" or "U'" or "U2":
			
				self.read_in_colours("X")

				if move == "U":
					self.turn_front("F")

				if move == "U'":
					self.turn_front("F'")
				
				if move == "U2":
					self.turn_front("F2")
				
				self.read_in_colours("X'")
				
			if move == "D" or "D'" or "D2":
			
				self.read_in_colours("X")

				if move == "D":
					self.turn_front("B")

				if move == "D''":
					self.turn_front("B'")
				
				if move == "D2":
					self.turn_front("B2")

				self.read_in_colours("X'")

			if move == "X" or "X'" or "Y" or "Y'" or "Z" or "Z'":
				
				if move == "Y":
					
					self.read_in_colours("Z")
					self.read_in_colours("X")
					self.read_in_colours("Z'")
					
				elif move == "Y'":
					
					self.read_in_colours("Z'")
					self.read_in_colours("X")
					self.read_in_colours("Z")
					
				else:
				
					self.read_in_colours(move)
		
                        print('Performing {} motion on cube'.format(move))

