#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2


def lidar_callback(data):
    rospy.loginfo("I've received lidar data")
    

if __name__ == '__main__':
	try:
		rospy.init_node('slam', anonymous=True)
		rospy.Subscriber("/points_raw", PointCloud2, lidar_callback)
		    
		map_pub = rospy.Publisher('/map', PointCloud2, queue_size=10)
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
		############# SLAM CODE :) #####################
			_map = PointCloud2()
			_map.data = [1,1,1,1,1]
			map_pub.publish(_map)
			rate.sleep()

	except rospy.ROSInterruptException:
		pass



