import rclpy
from rclpy.node import Node
from custom_interfaces.srv import FindClosestWall
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan

class Navigator(Node):
    def __init__(self):
        super().__init__('navigator_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.client = self.create_client(FindClosestWall, 'find_closest_wall')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.request = FindClosestWall.Request()
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        response = self.future.result()
        if response.successful:
            self.subscriber = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        else:
            self.get_logger().info('Server returned a negative response, aborting...')
            nav.destroy_node()
            rclpy.shutdown()
    
    def scan_callback(self, data:LaserScan):
        msg = Twist()
        msg.linear = Vector3()
        msg.angular = Vector3()
        if data.ranges[0] < 0.5:
            msg.linear.x = 0.0
            msg.angular.z = -0.35
        elif data.ranges[25] < 0.55:
            msg.linear.x = 0.0
            msg.angular.z = -0.15
        else:
            msg.linear.x = 0.25
            msg.angular.z = 0.0
        self.publisher.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)
    nav = Navigator()
    rclpy.spin(nav)
    nav.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()