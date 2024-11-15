#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def listener(msg:String):
    rospy.loginfo("I heard :" + str(msg.data))

def main():
    rospy.init_node("listener")
    sub = rospy.Subscriber("/chatter",String,callback=listener)
    rospy.loginfo("node has started")
    rospy.spin()

if __name__ == "__main__":
    main()
    