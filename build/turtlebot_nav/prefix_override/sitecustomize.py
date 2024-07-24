import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fourfold/dev/inmind sessions/inmind-session-7/turtlebot-navigation/install/turtlebot_nav'
