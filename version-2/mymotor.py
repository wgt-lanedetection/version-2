from gpiozero import Robot
from gpiozero import Motor
from gpiozero import Servo
from time import sleep



# Initialise GPIO for the motors
driveGPIO_fl1	=  24   #reartmotor left  forward
driveGPIO_fl2	=  23	#rearmotor  left  backward
driveGPIO_fr1	=  20	#reartmotor right forward
driveGPIO_fr2	=  16	#reartmotor right backward
steeringGPIO_l1	=  17	#frontomor  left  forward
steeringGPIO_l2	=  27	#frontomor  left  backward
steeringGPIO_r1	=  6	#frontomor  right forward
steeringGPIO_r2	=  5	#frontomor  right forward


# Initialise GPIO for Servo
servoGPIO =  17
min_angle = -45
max_angle =  45

# Define Motor driver Variables
m_drive = Robot((driveGPIO_fl1,driveGPIO_fl2), (driveGPIO_fr1,driveGPIO_fr2))
m_left	= Motor(steeringGPIO_l1,steeringGPIO_l2)
m_right	= Motor(steeringGPIO_r1,steeringGPIO_r2)
#servo 	= AngularServo(servoGPIO, min_angle, max_angle)


# drive forward  - rear drive
def drive(speed):
	m_drive.forward(speed)

# steering left motor
def drive_left(s_left):
	m_left.forward(s_left)

#steering right motor
def drive_right(s_right):
	 m_right.forward(s_right)
 
#Servo angle 
def steering_servo(s_angle):
	servo.angle = s_angle


