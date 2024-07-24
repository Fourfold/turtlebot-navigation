# Robotics Assignment - Session 7 - ROS2

**Firas Dimashki**

To build the project, enter the following commands while in the directory of the repository:
```
source install/setup.bash
colcon build
```
---
Then, to run the project, first run the Gazebo simulator in its directory (depends on the machine):
```
source install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_dqn_stage1.launch.py
```
Then enter the following in the repo directory:
```
ros2 launch launch/launch.py
```
---
When the project is launched, the service and action servers are up and running. The service is directly called upon running, and the action is called after 30 seconds for the robot to start its lap navigation.

First, the robot turns in the direction of the closest wall, then, it starts to navigate along the wall while making sure it does not collide with any walls.

When the LapTime action client sends its goal to the server after 30 seconds, the server first waits for the robot to reach one of four starting points (the midpoint along each wall), then it starts giving feedback about the elapsed time twice every second.

When the robot finishes a complete lap, the total lap time is logged, and the action client is destoyed.
