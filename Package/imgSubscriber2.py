#!/usr/bin/env python
#coding:utf-8

import rospy
import cv2
import cv_bridge
#from sensor_msgs.msg import Image
from image_transfer.msg import Image

def callback(data):
    bridge = cv_bridge.CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data,"bgr8")
    cv2.imshow("Received!!",cv_image)
    cv2.waitKey(0)

def showImage():
    rospy.init_node('midTransfer',anonymous = True)
    rospy.Subscriber('midTransfer', Image, callback)
    rospy.spin()


if __name__ == '__main__':
    showImage()