import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from custom_interfaces.action import MeasureLapTime
from nav_msgs.msg import Odometry
import time

class LapTimeServer(Node):
    def __init__(self):
        super().__init__('lap_time_server')
        self.action_service = ActionServer(self, MeasureLapTime, 'lap_time', self.execute_callback)
        self.reentrant_group = ReentrantCallbackGroup()
        self.subscriber = self.create_subscription(
            Odometry,
            '/odom',
            self.odometry_callback,
            10,
            callback_group=self.reentrant_group
        )
        self.x = 2
        self.y = 2
        self.feedback_time_period = 0.5
        time.sleep(30)
        self.get_logger().info('LapTime server started. Ready for requests.')

    def odometry_callback(self, odometry:Odometry):
        self.x = odometry.pose.pose.position.x
        self.y = odometry.pose.pose.position.y
        self.current_time = odometry.header.stamp.sec + 0.000000001 * odometry.header.stamp.nanosec

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Received LapTime request. Waiting for robot to reach starting point...')

        while abs(self.x) > 0.1 and abs(self.y) > 0.1:
            pass
        while abs(self.x) < 0.1 or abs(self.y) < 0.1:
            pass

        feedback_msg = MeasureLapTime.Feedback()
        self.start_time = self.current_time

        def timer_callback():
            feedback_msg.elapsed_time = self.current_time - self.start_time
            goal_handle.publish_feedback(feedback_msg)
        
        self.timer = self.create_timer(
            self.feedback_time_period,
            timer_callback,
            callback_group=self.reentrant_group
        )

        for _ in range(4):
            while abs(self.x) > 0.1 and abs(self.y) > 0.1:
                pass
            while abs(self.x) < 0.1 or abs(self.y) < 0.1:
                pass
            

        result = MeasureLapTime.Result()
        result.total_time = self.current_time - self.start_time

        goal_handle.succeed()

        return result

def main(args=None):
    rclpy.init(args=args)
    lap_time_server = LapTimeServer()

    executor = rclpy.executors.MultiThreadedExecutor(num_threads=3)
    executor.add_node(lap_time_server)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    lap_time_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()