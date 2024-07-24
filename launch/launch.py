from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_nav',
            executable='navigator_node',
            name='navigator_node'
        ),
        Node(
            package='turtlebot_nav',
            executable='find_closest_wall_server',
            name='find_closest_wall_server'
        ),
        Node(
            package='turtlebot_nav',
            executable='lap_server',
            name='lap_server'
        ),
        Node(
            package='turtlebot_nav',
            executable='lap_client',
            name='lap_client'
        ),
    ])
