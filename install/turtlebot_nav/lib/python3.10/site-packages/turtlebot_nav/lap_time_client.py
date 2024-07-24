import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from custom_interfaces.action import MeasureLapTime
import time

class LapTimeClient(Node):
    def __init__(self):
        super().__init__('lap_time_client')
        self.action_client = ActionClient(self, MeasureLapTime, 'lap_time')
    
    def send_goal(self):
        goal_msg = MeasureLapTime.Goal()
        self.action_client.wait_for_server()
        self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('LapTime goal rejected.')
            return

        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Total lap time: {round(result.total_time, 3)} seconds')
        self.destroy_node()
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Elapsed time: {round(feedback.elapsed_time, 3)} seconds')


def main(args=None):
    time.sleep(30)
    rclpy.init(args=args)
    lap_time_client = LapTimeClient()

    future = lap_time_client.send_goal()
    rclpy.spin(lap_time_client)


if __name__ == '__main__':
    main()