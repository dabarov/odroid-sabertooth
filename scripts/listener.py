#!/usr/bin/env python

import rospy
import serial

from sensor_msgs.msg import Joy


ss = serial.Serial(port="/dev/ttyS1",
                   baudrate=9600,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
                   timeout=1)


def map_x(x, min_in, max_in, min_out, max_out):
    return min_out + (x - min_in) * (max_out-min_out)/(max_in-min_in)


def to_bytes(n, length, byteorder='little'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if byteorder == 'big' else s[::-1]


def from_bytes(string, byteorder='little'):
    string = string if byteorder == 'big' else string[::-1]
    return int(string.encode('hex'), 16)


def callback(data):
    [a, b, c, d, _, _, _, _, _, _, _, _] = data.buttons
    [ls, lud, rs, rud, bs, bud] = data.axes
    if a == 1:  # Full stop
        motorA = map_x(0, 100, -100, 0, 127)
        motorB = map_x(0, 100, -100, 128, 255)
    elif bud == 1 or bud == -1:
        motorA = map_x(bud*20, 100, -100, 0, 127)
        motorB = map_x(bud*20, 100, -100, 128, 255)
    elif bs == 1 or bs == -1:
        motorA = map_x(bs*20, 100, -100, 0, 127)
        motorB = map_x(bs*(-20), 100, -100, 128, 255)
    elif ls:
        motorA = map_x(ls*100, 100, -100, 0, 127)
        motorB = map_x(ls*(-100), 100, -100, 128, 255)
    else:
        motorA = map_x(lud*100, 100, -100, 0, 127)
        motorB = map_x(lud*100, 100, -100, 128, 255)

    rospy.loginfo('Motor A and B: %s', (motorA, motorB))

    ss.write(to_bytes(motorA, 1, byteorder='little'))
    ss.write(to_bytes(motorB, 1, byteorder='little'))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
