ttyUSB_USB2DYNAMIXEL = "/dev/ttyUSB0"

DXL_LIB_PATH = "/home/chetanborse1999/DynamixelSDK/c/build/linux64/libdxl_x64_c.so"


ENABLE_DXL_MESSAGES = True
ENABLE_DEBUG_MESSAGES = True



# Servo Props
servoId = [7,15,8,9,17,1,11,18]
SERVO_RES = 0.2932551319648094

#Set-Point of Each Servo
FixedPoints = [190,200,512,500,480,760,500,500]  
# Direction of Motion
dirVector = [1,1,1,1,1,1,1,1]

# Venom Props

linkLength = [5.5,0,8.3,14.1]
# linkLength = [1,0,1,1]

# Reference Constants
A = 0
B = 3
C = 6
D = 9
TOP = 0
MIDDLE = 1
BOTTOM = 2
