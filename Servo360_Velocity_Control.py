from machine import Pin, PWM
import time

# Constants
PWM_FREQ = 50
PERIOD_US = 1000000 // PWM_FREQ  # 20000 us for 50 Hz
MIN_US = 1000  # 1 ms
MAX_US = 2000  # 2 ms

# Helper function to convert microsecond pulse width to duty cycle
def us_to_duty(us, period_us):
    return int((us / period_us) * 65535)

# Initialize servos
servo1 = PWM(Pin(0), freq=PWM_FREQ)
servo2 = PWM(Pin(1), freq=PWM_FREQ)

# Function to set servo pulse width
def write_us(servo, pulse_us):
    duty_cycle = us_to_duty(pulse_us, PERIOD_US)
    servo.duty_u16(duty_cycle)

# Set servos using microsecond pulse width
write_us(servo1, 1500)  # Center position
write_us(servo2, 1500)  # Center position
time.sleep(0.3)
write_us(servo1, 1000)  # Min position
write_us(servo2, 1000)  # Min position

