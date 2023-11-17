#!/usr/bin/python3

import rospy
from std_msgs.msg import String

class CaesarCipherDecryptor:
    def __init__(self):
        rospy.init_node('caesar_cipher_decryptor', anonymous=True)
        self.sub = rospy.Subscriber('/encrypted_name', String, self.callback)
        self.pub = rospy.Publisher('/decrypted_name', String, queue_size=10)

    def decrypt_name(self, encrypted_name):
        shift = 3  

        decrypted_name = ''.join(
            chr((ord(char) - shift - ord('a') + 26) % 26 + ord('a'))
            if 'a' <= char <= 'z' else
            char
            for char in encrypted_name
        )

        return decrypted_name

    def callback(self, data):
        encrypted_name = data.data
        decrypted_name = self.decrypt_name(encrypted_name)

        rospy.loginfo(f"Encrypted Name: {encrypted_name}") # found this on the roswiki its used for looking at the logs easy for us to look the output here
        rospy.loginfo(f"Decrypted Name: {decrypted_name}")

        self.pub.publish(decrypted_name)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    decryptor = CaesarCipherDecryptor()
    decryptor.run()
