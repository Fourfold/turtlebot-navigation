from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtlebot_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fourfold',
    maintainer_email='fourfold164@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "navigator_node = turtlebot_nav.navigator:main",
            "find_closest_wall_server = turtlebot_nav.closest_wall_server:main",
            "lap_server = turtlebot_nav.lap_time_server:main",
            "lap_client = turtlebot_nav.lap_time_client:main"
        ],
    },
)
