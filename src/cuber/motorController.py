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
		self.straight_ft = 695
		self.straight_fb = 150
		self.arm_botf = 125
		self.arm_midf = 450
		self.arm_midfa = 385
		self.arm_topf = 695

		self.straight_lt = 670
		self.straight_lb = 140
		self.arm_botl = 120
		self.arm_midl = 410
		self.arm_midla = 380
		self.arm_topl = 680

		self.straight_rt = 675
		self.straight_rb = 150
		self.arm_botr = 135
		self.arm_midra = 395
		self.arm_midr = 430
		self.arm_topr = 700

		self.straight_bt = 695
		self.straight_bb = 170
		self.arm_botb = 150
		self.arm_midba = 400
		self.arm_midb = 430
		self.arm_topb = 700

		self.arm_out = 200
		self.arm_inf = 360
		self.arm_inr = 365
		self.arm_inb = 390
		self.arm_inl = 365

		self.turn_straightf = 420
		self.turn_straightfa = 430
		self.turn_straightl = 400
		self.turn_straightla = 410 
		self.turn_straightr = 410
		self.turn_straightra = 400
		self.turn_straightb = 420
		self.turn_straightba = 420

		
		self.pwm.set_pwm_freq(60)

		self.pwm.set_pwm(0, 0, self.arm_out)
		self.pwm.set_pwm(4, 0, self.arm_out)	
		time.sleep(0.75)
		self.pwm.set_pwm(1, 0, self.straight_lb)
		self.pwm.set_pwm(5, 0, self.straight_rb)
		time.sleep(0.75)
		self.pwm.set_pwm(0, 0, self.arm_inl)
		self.pwm.set_pwm(4, 0, self.arm_inr)
		time.sleep(0.5)

		self.pwm.set_pwm(2, 0, self.arm_out)
		self.pwm.set_pwm(6, 0, self.arm_out)	
		time.sleep(0.75)
		self.pwm.set_pwm(3, 0, self.straight_fb)
		self.pwm.set_pwm(7, 0, self.straight_bb)
		time.sleep(0.75)
		self.pwm.set_pwm(2, 0, self.arm_inf)
		self.pwm.set_pwm(6, 0, self.arm_inb)
		time.sleep(0.5)

		self.move_armf = self.straight_fb
		self.move_arml = self.straight_lb
		self.move_armr = self.straight_rb
		self.move_armb = self.straight_bb

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
				
		if move == "X":
			
			if self.move_arml == self.arm_botl or self.move_arml == self.straight_lb:

				self.pwm.set_pwm(0, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, self.straight_lt)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, self.arm_inl)
				time.sleep(1)
				
			if self.move_armr == self.arm_topr or self.move_armr == self.straight_rt:

				self.pwm.set_pwm(4, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, self.straight_rb)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, self.arm_inr)
				time.sleep(1)
			
			self.pwm.set_pwm(2, 0, self.arm_out)
			self.pwm.set_pwm(6, 0, self.arm_out)	
			self.pwm.set_pwm(0, 0, 385)
			self.pwm.set_pwm(4, 0, 395)
			time.sleep(1)		
			self.pwm.set_pwm(1, 0, self.turn_straightla)
			self.pwm.set_pwm(5, 0, self.turn_straightr)
			self.pwm.set_pwm(3, 0, self.straight_fb)
			self.pwm.set_pwm(7, 0, self.straight_bb)
			time.sleep(1)
			self.pwm.set_pwm(2, 0, self.arm_inf)
			self.pwm.set_pwm(6, 0, self.arm_inb)
			time.sleep(1)
			
			self.pwm.set_pwm(0, 0, self.arm_out)
			self.pwm.set_pwm(4, 0, self.arm_out)
			time.sleep(1)		
			self.pwm.set_pwm(1, 0, self.straight_lb)
			self.pwm.set_pwm(5, 0, self.straight_rb)
			time.sleep(1)
			self.pwm.set_pwm(0, 0, self.arm_inl)
			self.pwm.set_pwm(4, 0, self.arm_inr)		
			
			self.arml = self.straight_lb
			self.armr = self.straight_rb
			self.armf = self.straight_fb
			self.armb = self.straight_bb
					
		elif move == "X'":
			
			if self.move_arml == self.arm_topl or self.move_arml == self.straight_lt:

				self.pwm.set_pwm(0, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, self.straight_lb)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, self.arm_inl)
				time.sleep(1)
				
			if self.move_armr == self.arm_botr or self.move_armr == self.straight_rb:

				self.pwm.set_pwm(4, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, self.straight_rt)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, self.arm_inr)
				time.sleep(1)
			
			self.pwm.set_pwm(2, 0, self.arm_out)
			self.pwm.set_pwm(6, 0, self.arm_out)
			self.pwm.set_pwm(0, 0, 385)
			self.pwm.set_pwm(4, 0, 395)
			time.sleep(1)		
			self.pwm.set_pwm(1, 0, self.turn_straightl)
			self.pwm.set_pwm(5, 0, self.turn_straightra)
			self.pwm.set_pwm(3, 0, self.straight_fb)
			self.pwm.set_pwm(7, 0, self.straight_bb)
			time.sleep(1)
			self.pwm.set_pwm(2, 0, self.arm_inf)
			self.pwm.set_pwm(6, 0, self.arm_inb)
			time.sleep(1)
			
			self.pwm.set_pwm(0, 0, self.arm_out)
			self.pwm.set_pwm(4, 0, self.arm_out)
			time.sleep(1)		
			self.pwm.set_pwm(1, 0, self.straight_lb)
			self.pwm.set_pwm(5, 0, self.straight_rb)
			time.sleep(1)
			self.pwm.set_pwm(0, 0, self.arm_inl)
			self.pwm.set_pwm(4, 0, self.arm_inr)		
			
			self.arml = self.straight_lb
			self.armr = self.straight_rb
			self.armf = self.straight_fb
			self.armb = self.straight_bb
		
		elif move == "Z":
			
			if self.move_armf == self.arm_topf or self.move_armf == self.straight_ft:

				self.pwm.set_pwm(2, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, self.straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, self.arm_inf)
				time.sleep(1)
				
			if self.move_armb == self.arm_botb or self.move_armb == self.straight_bb:

				self.pwm.set_pwm(6, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, self.straight_bt)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, self.arm_inb)
				time.sleep(1)
			
			self.pwm.set_pwm(0, 0, self.arm_out)
			self.pwm.set_pwm(4, 0, self.arm_out)
			self.pwm.set_pwm(2, 0, 390)
			self.pwm.set_pwm(6, 0, 420)
			time.sleep(1)		
			self.pwm.set_pwm(3, 0, self.turn_straightf)
			self.pwm.set_pwm(7, 0, self.turn_straightba)
			self.pwm.set_pwm(1, 0, self.straight_lb)
			self.pwm.set_pwm(5, 0, self.straight_rb)
			time.sleep(1)
			self.pwm.set_pwm(0, 0, self.arm_inf)
			self.pwm.set_pwm(4, 0, self.arm_inb)
			time.sleep(1)
			
			self.pwm.set_pwm(2, 0, self.arm_out)
			self.pwm.set_pwm(6, 0, self.arm_out)
			time.sleep(1)		
			self.pwm.set_pwm(3, 0, self.straight_fb)
			self.pwm.set_pwm(7, 0, self.straight_bb)
			time.sleep(1)
			self.pwm.set_pwm(2, 0, self.arm_inf)
			self.pwm.set_pwm(6, 0, self.arm_inb)		
			
			self.arml = self.straight_lb
			self.armr = self.straight_rb
			self.armf = self.straight_fb
			self.armb = self.straight_bb
		
		elif move == "Z'":
			
			if self.move_armf == self.arm_botf or self.move_armf == self.straight_fb:

				self.pwm.set_pwm(2, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, self.straight_ft)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, self.arm_inf)
				time.sleep(1)
				
			if self.move_armb == self.arm_topb or self.move_armb == self.straight_bt:

				self.pwm.set_pwm(6, 0, self.arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, self.straight_bb)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, self.arm_inb)
				time.sleep(1)
			
			self.pwm.set_pwm(0, 0, self.arm_out)
			self.pwm.set_pwm(4, 0, self.arm_out)	
			self.pwm.set_pwm(2, 0, 390)
			self.pwm.set_pwm(6, 0, 420)
			time.sleep(1)		
			self.pwm.set_pwm(3, 0, self.turn_straightfa)
			self.pwm.set_pwm(7, 0, self.turn_straightb)
			self.pwm.set_pwm(1, 0, self.straight_lb)
			self.pwm.set_pwm(5, 0, self.straight_rb)
			time.sleep(1)
			self.pwm.set_pwm(0, 0, self.arm_inl)
			self.pwm.set_pwm(4, 0, self.arm_inr)
			time.sleep(1)
			
			self.pwm.set_pwm(2, 0, self.arm_out)
			self.pwm.set_pwm(6, 0, self.arm_out)
			time.sleep(1)		
			self.pwm.set_pwm(3, 0, self.straight_fb)
			self.pwm.set_pwm(7, 0, straight_bb)
			time.sleep(1)
			self.pwm.set_pwm(2, 0, self.arm_inf)
			self.pwm.set_pwm(6, 0, self.arm_inb)		
			
			self.arml = self.straight_lb
			self.armr = self.straight_rb
			self.armf = self.straight_fb
			self.armb = self.straight_bb		
		
	def turn_front(self, move):
			
		if move == "F":

			if move_armf == arm_topf or move_armf == straight_ft:
		
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, arm_midf)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)		
				self.move_armf = straight_fb
				
			elif move_armf == arm_botf or move_armf == straight_fb:
		
				self.pwm.set_pwm(3, 0, arm_midf)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)
				self.move_armf = straight_fb

		elif move == "F'":
				
			if move_armf == arm_botf or move_armf == straight_fb:
				
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_ft)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, arm_midfa)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)
				self.move_armf = straight_fb
			
			elif move_armf == arm_topf or move_armf == straight_ft:
			
				self.pwm.set_pwm(3, 0, arm_midfa)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(3, 0, straight_fb)
				time.sleep(1)
				self.pwm.set_pwm(2, 0, arm_inf)
				self.move_armf = straight_fb

		elif move == "F2":
					
			if move_armf == arm_botf or move_armf == straight_fb:
			
				self.pwm.set_pwm(3, 0, arm_topf)
				self.move_armf = arm_topf
			
			elif move_armf == arm_topf or move_armf == sraight_ft:
			
				self.pwm.set_pwm(3, 0, arm_botf)
				self.move_armf = arm_botf

	def turn_right(self, move):

		if move == "R":
		
			if move_armr == arm_topr or move_armr == straight_rt:

				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rb)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midr)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midr-10)
				time.sleep(0.5)
				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rb)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				self.move_armr = straight_rb
				
			elif move_armr == arm_botr or move_armr == straight_rb:
				
				self.pwm.set_pwm(5, 0, arm_midr)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midr-10)
				time.sleep(0.5)
				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rb)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				self.move_armr = straight_rb

		elif move == "R'":
				
			if move_armr == arm_botr or move_armr == straight_rb:

				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rt)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midra)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midra+15)
				time.sleep(0.5)
				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rt)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				self.move_armr = straight_rt
				
			elif move_armr == arm_topr or move_armr == straight_rt:
				
				self.pwm.set_pwm(5, 0, arm_midra)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, arm_midra+15)
				time.sleep(0.5)
				self.pwm.set_pwm(4, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(5, 0, straight_rt)
				time.sleep(1)
				self.pwm.set_pwm(4, 0, arm_inr)
				self.move_armr = straight_rt

		elif move == "R2":
		
			if move_armr == arm_botr or move_armr == straight_rb:
			
				self.pwm.set_pwm(5, 0, arm_topr)
				self.move_armr = arm_topr
			
			elif move_armr == arm_topr or move_armr == straight_rt:
			
				self.pwm.set_pwm(5, 0, arm_botr)
				self.move_armr = arm_botr

	def turn_left(self, move):

		if move == "L":
		
			if move_arml == arm_topl or move_arml == straight_lt:

				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lb)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, arm_midl)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lb)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				move_arml = straight_lb
				
			elif move_arml == arm_botl or move_arml == straight_lb:
				
				self.pwm.set_pwm(1, 0, arm_midl)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lb)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				move_arml = straight_lb

		elif move == "L'":
				
			if move_arml == arm_botl or move_arml == straight_lb:

				if move_arml == arm_botl:
					
					self.pwm.set_pwm(1, 0, straight_lb)
					
				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lt)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, arm_midla)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lt)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				self.move_arml = straight_lt
				
			elif move_arml == arm_topl or move_arml == straight_lt:

				self.pwm.set_pwm(1, 0, arm_midla)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(1, 0, straight_lt)
				time.sleep(1)
				self.pwm.set_pwm(0, 0, arm_inl)
				self.move_arml = straight_lt

		elif move == "L2":
						
			if move_arml == arm_botl or move_arml == straight_lb:
			
				self.pwm.set_pwm(1, 0, arm_topl)
				self.move_arml = arm_topl
			
			elif move_arml == arm_topl or move_arml == straight_lt:
			
				self.pwm.set_pwm(1, 0, arm_botl)
				self.move_arml = arm_botl

	def turn_back(self, move):
	
		if move == "B":
		
			if move_armb == arm_topb or move_armb == straight_bt:
		
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bb)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_inb)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, arm_midb)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bb)
				time.sleep(1)
				self.pwm.sself.et_pwm(6, 0, arm_inb)		
				self.move_armb = straight_bb
				
			elif move_armb == arm_botb or move_armb == straight_bb:
		
				self.pwm.set_pwm(7, 0, arm_midb)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bb)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_inb)
				self.move_armb = straight_bb

		elif move == "B'":
				
			if move_armb == arm_botb or move_armb == straight_bb:
		
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bt)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_inb)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, arm_midba)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bt)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_inb)		
				self.move_armb = straight_bt
				
			elif move_armb == arm_topb or move_armb == straight_bt:
		
				self.pwm.set_pwm(7, 0, arm_midba)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_out)
				time.sleep(1)
				self.pwm.set_pwm(7, 0, straight_bt)
				time.sleep(1)
				self.pwm.set_pwm(6, 0, arm_inb)
				self.move_armb = straight_bt

		elif move == "B2":
					
			if move_armb == arm_botb or move_armb == straight_bb:
			
				self.pwm.set_pwm(7, 0, arm_topb)
				self.move_armb = arm_topb
			
			elif move_armb == arm_topb or move_armb == straight_bt:
			
				self.pwm.set_pwm(7, 0, arm_botb)
				self.move_armb = arm_botb

	def MotorControlString(self, motion):
	
		array = motion.split(' ')
		
		for move in array:
			
#			if move == "F" or move == "F'" or move == "F2":
		
#				self.turn_front(move)
		
#			elif move == "R" or move == "R'" or move == "R2":
				
#				self.turn_right(move)
				
#			elif move == "L" or move == "L'" or move == "L2":
				
#				self.turn_left(move)
				
#			elif move == "B" or move == "B'" or move == "B2":
				
#				self.turn_back(move)
				
#			elif move == "U" or move == "U'" or move == "U2":

#				self.read_in_colours("X")
#				time.sleep(1)
				
#				if move == "U":
#					turn_back("B")

#				elif move == "U'":
#					self.turn_back("B'")
				
#				elif move == "U2":
#					self.turn_back("B2")
				
#				time.sleep(1)
#				self.read_in_colours("X'")
				
#			elif move == "D" or move == "D'" or move == "D2":
				
#				self.read_in_colours("X")
#				time.sleep(1)
				
#				if move == "D":
#					self.turn_front("F")

#				elif move == "D'":
#					self.turn_front("F'")
				
#				elif move == "D2":
#					self.turn_front("F2")
				
#				time.sleep(1)
#				self.read_in_colours("X'")

#			if move == "X" or move == "X'" or move == "Y" or move == "Y'" or move == "Z" or move == "Z'":
				
#				if move == "Y":
					
#					self.read_in_colours("Z")
#					time.sleep(1)
#					self.read_in_colours("X")
#					time.sleep(1)
#					self.read_in_colours("Z'")
					
#				elif move == "Y'":
				
#					self.read_in_colours("Z'")
#					time.sleep(1)
#					self.read_in_colours("X")
#					time.sleep(1)
#					self.read_in_colours("Z")
					
#				else:
#					self.read_in_colours(move)
					
			print(" ")
			print('Performed {} motion on cube'.format(move))
			print(" ")
