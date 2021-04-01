#!/usr/bin/env python

import os
import sys
import subprocess
# Recieved place from home_tour
place = sys.argv[1]

# Fetching the coordinates from config file
with open("config.txt", 'r') as read_obj:
    for line in read_obj:
        if place in line:
            coordinate_array = line.split('"')[1::2]
        elif place == "PREVIOUS":
            previous_file = open("data", "r")
            prev_coordinates = previous_file.readline()
            coordinate_array = prev_coordinates.split('"')[1::2]

#Assigning the goal position(px,py,pz) and orientation(ox,oy,oz,ow)
px = float(coordinate_array[0])
py = float(coordinate_array[1])
pz = float(coordinate_array[2])
ox = float(coordinate_array[3])
oy = float(coordinate_array[4])
oz = float(coordinate_array[5])
ow = float(coordinate_array[6])

robot_position = "x: "+str(px)+",y: "+str(py)+",z: "+str(pz)

robot_orientation = "x: "+str(ox)+",y: "+str(oy)+",z: "+str(oz)+",w: "+str(ow)

# Sending the assigned pose to navigation goal
cmd = """ros2 action send_goal /NavigateToPose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {Position}, orientation: {Orientation}}}" """
cmd = cmd.replace("Position", robot_position)
cmd = cmd.replace("Orientation",robot_orientation)

c = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
(out,err) = c.communicate()

if(out.find("SUCCEEDED") != -1):
      print("SUCCEEDED")
      # Create and Store the navigation succeeded goal pose in "previous data" file.
      f = open("data", "w+")
      f.write('"%f",' % px)
      f.write('"%f",' % py)
      f.write('"%f",' % pz)
      f.write('"%f",' % ox)
      f.write('"%f",' % oy)
      f.write('"%f",' % oz)
      f.write('"%f",' % ow)
      f.close()
else:
    print(out)
