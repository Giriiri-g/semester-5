#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import tkinter as tk

def publish():
    data = entry.get()
    count = len(data.split())
    pub.publish(f'Word Count: {count}')

def publisher():
    global pub
    rospy.init_node('publisher3', anonymous=True)
    pub = rospy.Publisher('withgui', String, queue_size=10)

    root = tk.Tk()
    root.title("Word Count Publisher")
    root.geometry("300x150")

    label = tk.Label(root, text="Enter a string:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)

    button = tk.Button(root, text="Publish", command=publish)
    button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
