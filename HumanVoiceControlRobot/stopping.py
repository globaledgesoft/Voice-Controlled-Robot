#!/usr/bin/env python

import rclpy
import os
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
	# Subscribe to /odom topic
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            1)
        self.subscription  

    # fetching current robot position(px,py,pz) and orientation(ox,oy,oz,ow) from /odom topic
    def listener_callback(self, msg):
        px = msg.pose.pose.position.x
        py = msg.pose.pose.position.y
        pz = msg.pose.pose.position.z
        ox = msg.pose.pose.orientation.x
        oy = msg.pose.pose.orientation.y
        oz = msg.pose.pose.orientation.z
        ow = msg.pose.pose.orientation.w
        robot_position = "x: "+str(px)+",y: "+str(py)+",z: "+str(pz)
        robot_orientation = "x: "+str(ox)+",y: "+str(oy) + \
            ",z: "+str(oz)+",w: "+str(ow)
	# Sending the assigned pose to navigation goal
        cmd = """ros2 action send_goal /NavigateToPose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {Position}, orientation: {Orientation}}}" """
        cmd = cmd.replace("Position", robot_position)
        cmd = cmd.replace("Orientation", robot_orientation)

        os.system(cmd)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin_once(minimal_subscriber)

    # Destroy the node explicitly
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
