# based on https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
# Import mavutil
from pymavlink import mavutil


def set_servo_pwm(servo_n, microseconds):
    """ Sets AUX 'servo_n' output PWM pulse-width.
   Uses https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
   'servo_n' is the AUX port to set (assumes port is configured as a servo).
        Valid values are 1-3 in a normal BlueROV2 setup, but can go up to 8
        depending on Pixhawk type and firmware.
    'microseconds' is the PWM pulse-width to set the output to. Commonly
        between 1100 and 1900 microseconds.
   """
    # master.set_servo(servo_n+8, microseconds) or:
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        servo_n,  # servo instance,
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        direction = str(msg.data)
        if(direction == ""):
            #do not call anything
        if(direction == "right"):
            #right thruster clockwise
            #left thruster counter clockwise
            backward = [1200, 1250,1300,1350,1400,1450,1500,1550,1600,1650,1700, 1750]
            forward = [1500, 1550,1600,1650,1700,1750,1800,1850,1850,1850,1850,1850]
            for us in range(0, len(forward) 1):
                set_servo_pwm(3, backward[us])
                set_servo_pwm(2, forward[us])
                time.sleep(0.125)

        if(direction == "left"):
            #left thruster clockwise
            #right thruster counter clockwise
            backward = [1200, 1250,1300,1350,1400,1450,1500,1550,1600,1650,1700, 1750]
            forward = [1500, 1550,1600,1650,1700,1750,1800,1850,1850,1850,1850,1850]
            for us in range(0, len(forward) 1):
                set_servo_pwm(2, backward[us])
                set_servo_pwm(3, forward[us])
                time.sleep(0.125)

        if(direction == "forward"):
            #both thrusters clockwise:
            for us in range(1500, 1900, 50):
                set_servo_pwm(2, us)
                set_servo_pwm(3, us)
                time.sleep(0.125)

        if (direction == "stop"):
            # both thrusters counter clockwise
            for us in range(1100, 1500, 50):
                set_servo_pwm(2, us)
                set_servo_pwm(3, us)
                time.sleep(0.125)

def main(args=None):
    # Create the connection
    master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
    # Wait a heartbeat before sending commands
    master.wait_heartbeat()
    SERVO1_FUNCTION=0
    SERVO2_FUNCTION=0
    SERVO3_FUNCTION=0
    SERVO4_FUNCTION=0
    SERVO5_FUNCTION=0
    SERVO6_FUNCTION=0
    SERVO7_FUNCTION=0
    SERVO8_FUNCTION=0
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()