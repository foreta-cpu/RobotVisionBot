import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


right_motor_a = 17
right_motor_b = 18
right_motor_en = 12
left_motor_a = 22
left_motor_b = 23
left_motor_en = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)

GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en, 1000)
pwm_l = GPIO.PWM(left_motor_en, 1000)

pwm_r.start(75)
pwm_l.start(75)

# Функция для движения вперёд
def forward(second):
    print('Forward Moving')
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)

# Функция для движения назад
def reverse(second):
    print('Reverse Moving')
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)

# Функция для поворота вправо
def right(second):
    print('Right Moving')
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)

# Функция для поворота влево
def left(second):
    print('Left Moving')
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)

# Функция для остановки
def stop(second):
    print('Stopping Motors')
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)
    time.sleep(second)

def exit():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    right(2)
    left(2)
    stop(2)
    exit()
    
if __name__ == '__main__':
    main()