# SLAMEnvironment

Vehicle model with (3D lidar, IMU and Camera sensors) can be simulated in 2 different maps.
![ Vehicle ](https://github.com/BelalElhossany/SLAMEnvironment/blob/main/images/vehicle.PNG)

# How to run

1- Install ROS
  - melodic for UBUNTU 18
  - noetic for UBUNTU 20
 ```
 http://wiki.ros.org/ROS/Installation
 ```
 NOTE: Choose Desktop-Full Install in section 1.4 to install gazebo with ROS
 
 2- Create catkin workspace
 ```
 http://wiki.ros.org/catkin/Tutorials/create_a_workspace
 ```
 
 3- Clone the repo
 ```
 cd ~/catkin_ws/src
 git clone 
 ```
 
 4- Install dependencies
 ```
 cd ~/catkin_ws/src/vehicle_sim
 rosdep install --from-paths . -y
 ```
 
 5- Build
 ```
 catkin_make
 source "your catkin workspace"/devel/setup.bash
 ```
 6- upgrade gazebo version and download gazebo models
 ```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/gazebo-stable.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D2486D2DD83DB69272AFE98867170598AF249743
sudo apt update
sudo apt upgrade
 ```
 ```
 rosrun vehicle_sim_launcher setup.sh
 ```
 
 7- Run Simple walls environment
 ```
 roslaunch vehicle_sim_launcher walls.launch
 ```
 ![ Walls ](https://github.com/BelalElhossany/SLAMEnvironment/blob/main/images/walls.PNG)
 
 8- Run complex city environment
 ```
 roslaunch vehicle_sim_launcher city.launch
 ```
 ![ City ](https://github.com/BelalElhossany/SLAMEnvironment/blob/main/images/city.PNG)
 
 NOTE: add ```gpu:=true ``` to roslaunch command to use gpu.

-------------------------------------------------------------------------------------------
Once you launch it, 3 windows will pop up:
  - Gazebo Simulation.
  - RVIZ : For visualization, you will find:
    1- Car model.
    2- Colored points representing lidar readings.
    3- Funny arrow representing IMU readings.
    4- Image to show camera output.
    Your map needs to be added to the list :)
    
    ![ Rviz ](https://github.com/BelalElhossany/SLAMEnvironment/blob/main/images/rviz.PNG)
  - Window to control vehicle velocity and steering.
  - 
    ![ Vehicle ](https://github.com/BelalElhossany/SLAMEnvironment/blob/main/images/control.PNG)

-------------------------------------------------------------------------------------------
# Sample code
sample code exists in: ```~/catkin_ws/src/slam_code/scripts```
  - It subscribes to ```/points_raw``` topic which lidar publishes on.
  - Creates dumy PointCloud2 message to simulate the map which will be the output of the SLAM algorithm, then publishes it on ```/map``` topic.
  - Your SLAM code needs to be added to a script like this.

NOTE: This code is included in launch files, so runs once you do step 7 or 8.
