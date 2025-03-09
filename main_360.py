from machine import Pin, PWM
import time
# set pwm freq
PWM_FREQ = 50
# define servos with pwm
servo1 = PWM(Pin(0), freq=PWM_FREQ, duty_u16=0)
servo2 = PWM(Pin(1), freq=PWM_FREQ, duty_u16=0)
# function that runs motor with a certain duty cycle
def set_servo_pwm(servo, duty):
    servo.duty_u16(duty)
# define test PWM values
#test_duties = [8000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
duty = 6000
# data collection loop
#set speed on servo
set_servo_pwm(servo2, duty)
print(f"Testing duty cycle: {duty}")
# wait a second
time.sleep(20)

'''
for duty in test_duties:
    #set speed on servo
    set_servo_pwm(servo1, duty)
    print(f"Testing duty cycle: {duty}")
    # wait a second
    time.sleep(5)
    # manually measure speed and record it (or use sensor)
    measured_speed = input(f"Enter measured speed for duty {duty}: ")
    print(f"Duty: {duty}, Speed: {measured_speed} rotations for 10 seconds")
'''
# Stop motor
set_servo_pwm(servo1, PWM_FREQ)
print("Test complete, motor stopped.")
