import os

with open("config.txt", 'r') as read_obj:
    for line in read_obj:
        if 'INITIAL_POSE' in line:
            coordinate_array = line.split('"')[1::2]

px = float(coordinate_array[0])
py = float(coordinate_array[1])
pz = float(coordinate_array[2])
ox = float(coordinate_array[3])
oy = float(coordinate_array[4])
oz = float(coordinate_array[5])
ow = float(coordinate_array[6])

robot_position = "x: "+str(px)+",y: "+str(py)+",z: "+str(pz)

robot_orientation = "x: "+str(ox)+",y: "+str(oy)+",z: "+str(oz)+",w: "+str(ow)
# publishing the initial pose
cmd = """ros2 topic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped '{ header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: { pose: {position: {Position}, orientation: {Orientation}}, } }' """
cmd = cmd.replace("Position", robot_position)
cmd = cmd.replace("Orientation",robot_orientation)
os.system(cmd)
