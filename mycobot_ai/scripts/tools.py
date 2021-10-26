from pymycobot.mycobot import MyCobot

# name of device
port = "/dev/ttyUSB0"
mc = MyCobot(port)

# release mycobot
# mc.release_all_servos()

# calibrate the sixth servo
mc.set_servo_calibration(6)
