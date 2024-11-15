#include <iostream>
#include <sstream>
#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char **argv){
    ros::init(argc,argv,"talker");
    ros::NodeHandle nh;

    ros::Publisher talker_pub = nh.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(1);
    
    ROS_INFO("Node has started");
    loop_rate.sleep();
    int count = 0;
    while(ros::ok()){
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Hello World " << count;
        msg.data = ss.str();
        ROS_INFO("%s",msg.data.c_str());
        talker_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        ++count;
    }
    return 0;
}