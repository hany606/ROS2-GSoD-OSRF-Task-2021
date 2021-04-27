import rclpy
from rclpy.node import Node
from random import randint

from std_msgs.msg import Int16

class CustomerNode(Node):

    def __init__(self):
        super().__init__('customer_node')
        self.publisher_ = self.create_publisher(Int16, 'input', 10)
        self.subscription = self.create_subscription(
            Int16,
            'result',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def listener_callback(self, msg):
        self.get_logger().info(f'Recieved in {self.i-1}: {msg.data}')

    def timer_callback(self):
        msg = Int16()
        msg.data = randint(0,1000)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing in {self.i}: {msg.data}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    customer_node = CustomerNode()
    rclpy.spin(customer_node)

    customer_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
