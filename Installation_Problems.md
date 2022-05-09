!! Don't do any of these unless you have an error !!

# You don't need to explicitly install catkin
you don't need to follow link install catkin when creating catkin workspace
``` http://wiki.ros.org/catkin/Tutorials/create_a_workspace```
but if it's not already installed for any reason, install it using apt-get not from source.
  ROS melodic: ``` sudo apt-get install ros-melodic-catkin```
  ROS noetic: ``` sudo apt-get install ros-noetic-catkin```


# If you have packages of version python3 and when you catkin_make errors say any python package is not found 

First, make sure you have already installed python3 version of this package.

use this version of catkin_make to force using python3 in case version2 is the one used.
```catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.7m```

ROS melodic uses python2 by default.
ROS noetic uses python3 by default.

# If you using ROS noetic and get error about "xacro.py" no such command

``` cd ~/catkin_ws/src/SLAMEnvironment/vehicle_sim/launcher/vehicle_sim_launcher/launch ```

open file ```city.launch``` and ```walls.launch``` and remove ```.py``` from ```xacro.py```
from this line ```<param name="robot_description" command="$(find xacro)/xacro.py --inorder $(arg model) gpu:=$(arg gpu)" />```
