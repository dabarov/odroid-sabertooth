# Jaguar Odroid

## Getting started

1. Setup the joystick connected to your computer following [this tutorial](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick)

2. Insert IP addresses of the devices into their ```.bashrc``` files, as follows:

```c
export ROS_IP=192.168.1.115 // replace with coresponding IP here
```

3. Follow [this tutorial](http://wiki.ros.org/ROS/Tutorials/MultipleMachines) to setup connection between devices.

## Usage

1. Power the robot.
2. Launch ```roscore``` on your pc.
3. Connect to the odroid:

```c
ssh odroid@198.168.1.190 // replace with IP address of the odroid  
```

4. Run the listener script on the odroid:

```c
rosrun beginners_tutorial listener.py
```

5. Run the joy node on your PC:

```c
rosrun joy joy_node
```
