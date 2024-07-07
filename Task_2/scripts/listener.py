import rospy
from std_msgs.msg import String,Int16 ,Bool

def callback(My_string):
    rospy.loginfo("I heard %s" ,My_string.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber("chatter",String,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
        