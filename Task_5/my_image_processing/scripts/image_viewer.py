import rospy
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import sys

bridge = CvBridge() #create a bridge

def image_callback(ros_image):
    print ("got an image")
    global bridge
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, 'bgr8')
    except CvBridgeError as e:
        print (e)
    #from now you can work with opencv commands:
    cv2.imshow("Image window orginal", cv_image)
    edge_image = cv2.Canny(cv_image,200,250)
    cv2.imshow("Image window edge", edge_image)
    edge_ros_image = bridge.cv2_to_imgmsg(edge_image)
    image_pub.publish(edge_ros_image)

    cv2.waitKey(3)

def main(args):
    rospy.init_node("image_viewer", anonymous=True)
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    global image_pub
    image_pub = rospy.Publisher("/canny_image",Image,queue_size=10)
    try :
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv) 