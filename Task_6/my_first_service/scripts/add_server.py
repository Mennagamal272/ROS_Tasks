from my_first_service.srv import AddTwointsSrv
from my_first_service.srv import AddTwointsSrvRequest
from my_first_service.srv import AddTwointsSrvResponse
import time
import rospy

def handle_add_two_ints(req):
    print(f"Returning [{req.a} + {req.b} = {req.a + req.b}]")
    time.sleep(5)  # 5 seconds delay
    sum_response = AddTwointsSrvResponse(req.a + req.b)
    return sum_response

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwointsSrv, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
