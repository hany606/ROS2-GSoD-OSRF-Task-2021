import rclpy
from rclpy.node import Node
from random import randint

from std_msgs.msg import Int16
from custom_msg_interface.msg import Request

class MultiplierNode(Node):

    def __init__(self):
        super().__init__('multiplier_node')
        self.publisher_ = self.create_publisher(Int16, 'result', 10)
        self.subscription = self.create_subscription(
            Request,
            'input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
    def listener_callback(self, recv):
        self.get_logger().info(f'Recieved: {recv.num1}, {recv.num2}')
        msg = Int16()
        msg.data = recv.num1 * recv.num2
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    multiplier_node = MultiplierNode()
    rclpy.spin(multiplier_node)

    multiplier_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
