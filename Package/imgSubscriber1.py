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
    cv2.imshow("lala",cv_image)
    setImg(cv_image)
    cv2.waitKey(0)

def showImage():
    rospy.init_node('showImage',anonymous = True)
    rospy.Subscriber('ShowImage', Image, callback)
    rospy.spin()

def setImg(image):
    pub = rospy.Publisher('midTransfer', Image, queue_size=10)
    rate = rospy.Rate(10)
    bridge = cv_bridge.CvBridge()
    while not rospy.is_shutdown():
        pub.publish(bridge.cv2_to_imgmsg(image, "bgr8"))
        rate.sleep()

if __name__ == '__main__':
    showImage()