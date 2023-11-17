#!/usr/bin/python3

import rospy
from std_msgs.msg import String

rospy.init_node("caesar_cipher_publisher") #create a node

def change(name):
    result = ""
    shift = 3 #we can change this number and the encryption will change
    for char in name:
        result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def publisher():
    talker_pub = rospy.Publisher("/encrypted_name", String, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        name = input("Enter the name to encrypt: ") #enter the name to encrypt
        encrypted_name = change(name)
        talker_pub.publish(encrypted_name) #publish the name to the node
        rate.sleep()
if __name__ == '__main__':
    publisher() #run the publisher func

