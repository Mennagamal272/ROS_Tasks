# license removed for brevity
import rospy
from std_msgs.msg import String
from second_pkg.msg import V2V

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    car_pub = rospy.Publisher('car_channel',V2V, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)

    passat_car_info = V2V()
    passat_car_info.name = "Passat"
    
    while not rospy.is_shutdown():
        hello_str = "Hello World %s" % str(rospy.get_time())
        #rospy.loginfo(hello_str)
        pub.publish(String(hello_str))
        car_pub.publish(passat_car_info)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
