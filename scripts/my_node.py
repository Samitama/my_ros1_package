#!/usr/bin/env python3 
import rospy

if __name__ == '__main__':
	rospy.init_node("test_node") #Topic adı olarak tanımlanır.
	rospy.loginfo("Test node has started")

	rate = rospy.Rate(10)
	c = 0
	while not rospy.is_shutdown():
		rospy.loginfo("Hello world " + str(c))
		c = c + 1
		rate.sleep()
	#rospy.loginfo("Hello ROS world")
	#rospy.logwarn("This is a warning")
	#rospy.logerr("This is an error")
	#rospy.sleep(1)
	#rospy.loginfo("End of program")