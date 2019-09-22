#include "ros/ros.h"
#include "std_msgs/String.h"
#include "edo_core_msgs/CartesianPose.h"
#include "stdio.h"

#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<edo_core_msgs::CartesianPose>("/cartesian_pose", 1000);

  ros::Rate loop_rate(10);
  int count = 0;
  edo_core_msgs::CartesianPose msg;

  while (ros::ok())
  {
    msg.x = count++;

    chatter_pub.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
