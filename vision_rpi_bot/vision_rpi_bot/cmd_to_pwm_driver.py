import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Int16, 'pub_topic', self.cmd_to_pwm, 10)
        self.subscription  # prevent unused variable warning
        right_motor_a = 17
        right_motor_b = 18
        right_motor_en = 12
        left_motor_a = 22
        left_motor_b = 23
        left_motor_en = 13
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
    def cmd_to_pwm_callback(self, msg):
        

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()