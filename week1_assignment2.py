#!/usr/bin/env python
# This code has been adapted from the ROS Wiki ROS Service tutorials to the context
# of this course.
# (http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

import sys
import rospy
from hrwros_msgs.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse
from hrwros_msgs.msg import BoxHeightInformation

def box_height_info_callback(x):
    # First wait for the service to become available.
    rospy.loginfo("Waiting for service...")
    rospy.wait_for_service('metres_to_feet')
    rospy.loginfo("Service %s is now available", 'metres_to_feet')
    try:
        # Create a service proxy.
        metres_to_feet = rospy.ServiceProxy('metres_to_feet', ConvertMetresToFeet)

        # Call the service here.
        service_response = metres_to_feet(x.box_height)

        # Return the response to the calling function.
        if(not service_response.success):
            rospy.logerr("Conversion unsuccessful! Requested distance in metres should be a positive real number.")
        else:
            rospy.loginfo("%4.2f(m) = %4.2f feet" %(x.box_height, service_response.distance_feet))
            rospy.loginfo("Conversion successful!")


    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":

    # Initialize the client ROS node.
    rospy.init_node("box_height_in_feet", anonymous=False)

    # The distance to be converted to feet.
    rospy.Subscriber('box_height_info', BoxHeightInformation, box_height_info_callback)
    rospy.spin()
    # Process the service response and display log messages accordingly.
   
