#!/usr/bin/python3

import rospy
from std_msgs.msg import String

class DecryptedNameSubscriber:
    def __init__(self):
        rospy.init_node('decrypted_name_subscriber', anonymous=True)
        rospy.Subscriber('/decrypted_name', String, self.callback)

    def callback(self, data):
        decrypted_name = data.data
        rospy.loginfo(f"Received Decrypted Name: {decrypted_name}")

    def run(self):
        rospy.spin() #no clue how it works but apprently some fourm said that it doesnt let it exit the python program

if __name__ == '__main__':
        subscriber = DecryptedNameSubscriber()
        subscriber.run()
