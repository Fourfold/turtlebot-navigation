import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from custom_interfaces.srv import FindClosestWall
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan

class ClosestWallServer(Node):
    def __init__(self):
        super().__init__('closest_wall_server')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.reentrant_group = ReentrantCallbackGroup()
        self.subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10,
            callback_group=self.reentrant_group
        )
        self.service = self.create_service(FindClosestWall, 'find_closest_wall', self.find_closest_wall_callback)
        self.scanning = False
        self.scan_data = None
        self.get_logger().info('FindClosestWall server started. Ready for requests.')
    
    def scan_callback(self, data:LaserScan):
        if not self.scanning:
            return
        else:
            self.scan_data = data.ranges
            self.scanning = False
    
    def find_closest_wall_callback(self, request, response):
        self.get_logger().info('Incoming FindClosestWall request.')
        self.scanning = True
        while self.scanning:
            pass
        rotateRight = self.getRotationDirection()

        msg = Twist()
        msg.angular = Vector3()
        if rotateRight:
            msg.angular.z = -0.25
        else:
            msg.angular.z = 0.25
        self.publisher.publish(msg)

        done = False
        while not done:
            self.scanning = True
            while self.scanning:
                pass
            done = self.isCorrectDirection()
        
        msg.angular.z = 0.0
        self.publisher.publish(msg)

        self.get_logger().info('FindClosestWall request fulfilled. Sending response.')
        response.successful = True
        return response

    
    def getRotationDirection(self):
        closestIndex = 0
        closestDistance = self.scan_data[-4] + self.scan_data[-3] + self.scan_data[-2] + self.scan_data[-1] + self.scan_data[0] + self.scan_data[1] + self.scan_data[2] + self.scan_data[3] + self.scan_data[4]
        for i in range(1, 40):
            sum = 0
            for j in self.scan_data[9*i-4 : 9*(i+1)-4]:
                sum += j
            if closestDistance == -1 or sum < closestDistance:
                closestIndex = i
                closestDistance = sum
        if closestIndex < 20:
            return False
        else:
            return True
    
    def isCorrectDirection(self):
        forwardDistance = self.scan_data[-4] + self.scan_data[-3] + self.scan_data[-2] + self.scan_data[-1] + self.scan_data[0] + self.scan_data[1] + self.scan_data[2] + self.scan_data[3] + self.scan_data[4]
        for i in range(1, 40):
            sum = 0
            for j in self.scan_data[9*i-4 : 9*(i+1)-4]:
                sum += j
            if sum < forwardDistance:
                return False
        return True


def main(args=None):
    rclpy.init(args=args)
    closestWallServer = ClosestWallServer()

    executor = rclpy.executors.MultiThreadedExecutor(num_threads=2)
    executor.add_node(closestWallServer)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    closestWallServer.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()