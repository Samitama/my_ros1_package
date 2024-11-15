#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main():
	rospy.init_node("talker")
	pub = rospy.Publisher("/chatter", String, queue_size=10)
	rate = rospy.Rate(1)
	c = 0
	while not rospy.is_shutdown():
		rospy.loginfo("Hello world " + str(c))
		msg = String()
		msg.data = "Hello world " + str(c)
		c = c+1
		pub.publish(msg)
		rate.sleep()


if __name__ == "__main__":
	main()