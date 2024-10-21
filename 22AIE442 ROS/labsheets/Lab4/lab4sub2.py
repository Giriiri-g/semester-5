#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import tkinter as tk
from tkinter import messagebox

def callback(data):
    messagebox.showinfo("Received Message", f"Message: {data.data}")

def subscriber():
    rospy.init_node('subscriber2', anonymous=True)
    rospy.Subscriber('factorial', String, callback)

    root = tk.Tk()
    root.title("Factorial Subscriber")
    root.geometry("300x150")

    label = tk.Label(root, text="Subscriber is active. Listening...")
    label.pack(pady=20)

    while not rospy.is_shutdown():
        root.update()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
