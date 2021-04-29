import rclpy
from rclpy.node import Node
from random import randint

from std_msgs.msg import Int16
from custom_msg_interface.msg import Request

class CustomerNode(Node):

    def __init__(self):
        super().__init__('customer_node')
        self.publisher_ = self.create_publisher(Request, 'input', 10)
        self.subscription = self.create_subscription(
            Int16,
            'result',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.timer_period = 0.5  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.i = 0
        
    def listener_callback(self, msg):
        self.get_logger().info(f'Recieved in {self.i-1}: {msg.data}')

    def timer_callback(self):
        msg = Request()
        msg.num1 = randint(0,100)
        msg.num2 = randint(0,100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing in {self.i}: {msg.num1},{msg.num2}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    customer_node = CustomerNode()
    rclpy.spin(customer_node)

    customer_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
