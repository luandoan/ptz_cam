#!/usr/bin/env python

import rospy
import urllib2
import urllib2 as ul
import time
import cv2
from sensor_msgs.msg import Joy

def control_sunba(vertical, horizontal, zoom):
    if(horizontal>0):
	goRight()
	time.sleep(0.01)
	print("PTZ pan to the right")
    elif(horizontal<0):
	goLeft()
	time.sleep(0.01)
	print("PTZ pan to the left")
    elif(vertical>0):
	lookUp()
	time.sleep(0.01)
	print("PTZ look up")
    elif(vertical<0):
	lookDown()
	time.sleep(0.01)
	print("PTZ look down")
    elif(zoom>0):
	zoomTile()
	time.sleep(0.01)
	print("PTZ zooming in")
    elif(zoom<0):
	zoomWide()
	time.sleep(0.01)
	print("PTZ zooming out")
    elif(stop==1):
	stop()

def goRight():
    ip_right = 'http://10.10.10.13/?command=ptz_req&req=start&param=directionleft&channel=1&stream=0'
    URL_right = ip_right
    ip_stop = 'http://10.10.10.13/?command=ptz_req&req=stop&param=directionleft&channel=1&stream=0'
    URL_stop = ip_stop
    response = ul.urlopen(URL_right)
    rospy.Duration(0.5)
    response = ur.urlopen(URL_stop)
    #rospy.loginfo(fullURL)
	
def goLeft():
    ip_left = 'http://10.10.10.13/?command=ptz_req&req=start&param=directionright&channel=1&stream=0'
    URL_left = ip_left
    ip_stop = 'http://10.10.10.13/?command=ptz_req&req=stop&param=directionright&channel=1&stream=0'
    URL_stop = ip_stop    
    response = ul.urlopen(URL_left)
    rospy.Duration(0.5)
    response = ur.urlopen(URL_stop)
    #rospy.loginfo(fullURL)

def lookUp():
    ip_up = 'http://10.10.10.13/?command=ptz_req&req=start&param=directiondown&channel=1&stream=0'
    URL_up = ip_up
    response = ul.urlopen(URL_up)
    #rospy.loginfo(fullURL)

def lookDown():
    ip_down = 'http://10.10.10.13/?command=ptz_req&req=start&param=directionup&channel=1&stream=0'
    URL_down = ip_down
    response = ul.urlopen(URL_down)
    #rospy.loginfo(fullURL)

def zoomTile():
    ip_zoomIn = 'http://10.10.10.13/?command=ptz_req&req=start&param=zoomtile&channel=1&stream=0'
    URL_zoomIn = ip_zoomIn
    response = ul.urlopen(URL_zoomIn)
    #rospy.loginfo(fullURL)

def zoomWide():
    ip_zoomOut = 'http://10.10.10.13/?command=ptz_req&req=start&param=zoomwide&channel=1&stream=0'
    URL_zoomOut = ip_zoomOut
    response = ul.urlopen(URL_zoomOut)
    #rospy.loginfo(fullURL)

def stop():
    ip = 'http://10.10.10.13/?command=ptz_req&req=stop&param=directiondown&channel=1&stream=0'
    URL = ip
    response = ul.urlopen(URL)


def callback(data):
    rospy.loginfo(data)
    horizontal = data.buttons[4]*data.buttons[5]*data.axes[6]
    print "Horizontal: ", horizontal
    vertical = data.buttons[4]*data.buttons[5]*data.axes[7]
    print "Vertical: ", vertical
    zoom = data.buttons[4]*data.buttons[5]*data.axes[1]
    print "Zoom: ", zoom
    stop = data.buttons[4]*data.buttons[5]*data.buttons[2]
    print "Stop: ", stop

    # publish to control node
    control_sunba(vertical, horizontal, zoom)


def joySunba():
    rospy.init_node("joy_sunba", anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)

    rospy.spin()

if __name__== '__main__':
    joySunba()



