# Tutorial on how to connect and operate lidar on Raspberry Pi.

The YDLidar X4 can be run on either Windows or Linux/Ubuntu. Originally we attempted to run it directly on Debian (based on Raspbian) but encountered errors after attempting to install the ros drivers onto the computer. Consequently, we chose to download a disk image for the RasPi that had Ubuntu 16 and ROS Kinetic installed. This was handy as it saved us the trouble of installing ROS Kinetic manually. This disk image is avaliable at `https://downloads.ubiquityrobotics.com/pi.html`, we used the `2020-11-07-ubiquity-xenial-lxde` version, but if this is not the newest one at the time you access it, the newest one should also work fine. Once the disk image is flashed (we used the Raspberry Pi Imager available on their website to do this), make sure to set it up with the instructions outlined on the Ubiquity Robots link. I will repeate it here in case it is no longer avaliable at time of access.

On startup, the RasPi with the newly installed disk image will host and connect to its own wifi network called `ubiquityrobotXXXX` where the `XXXX` is part of the MAC address. The password for this wifi, by default is `robotseverywhere`. If you have an external monitor it is not neccesary to connect via SSH from a different computer, as everthing can be done directly on the monitor. However it may be beneficial to know how to do this anyway: Once the RasPi is booted up connect your secondary computer to the RasPis wifi network, open terminal and type `ssh ubuntu@10.42.0.1`. This obviously assumes that you have SSH set up on your computer. As default, the password is `ubuntu`, you will have to enter this before you are connected to the RasPi.

When logging in for the first time on a new flashed OS, it's always a good idea to upgrade the software before doing anything else, particularly if your next plans have heavy requirements. This is done with 

```bash
sudo apt-get update
sudo apt-get upgrade
```
##### Updating the keyboard and locale
We are using a German keyboard, so we will see here how to change it from the default US and updating the locale configuration (which control the text language etc of the OS, [see here for more](https://docs.oracle.com/cd/E19455-01/806-0169/6j9hsml2f/index.html)) as they don't seem to be setup correctly on the default image. First the keyboard layout can be set using `sudo dpkg-reconfigure keyboard-configuration`. You can then choose all of the right settings for your specific keyboard.

The next step is to setup the locale, without which you won't be able to use pip with python (for example) and will ruin many other settings you want to do. The commands to do are 

```bash
export LC_ALL=en_US.UTF-8
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
```

This should in principle fix all of those. A good test, that will then later become useful for the general project, is to remove the original GPIO pin control (as it's also not working for some reason, by running `sudo apt remove rpi.gpio`. This will completely remove it from the system and then you can reinstall it specifically for the python versions using pip: `pip3 install RPi.GPIO`. This should run without an error and you should then be able to go into the python interpreter and test `import RPi.GPIO`, which should now run without errors, contrarily to earlier.

##### Installing YDLidar-SDK

The RasPi disk image with Ubuntu 16 and ROS should be up and running. Now we have to install the drivers specific to the YDLidar X4. The general procedure is outlined in the YDLidar X4 user manual available at `https://www.ydlidar.com/Public/upload/files/2020-04-13/YDLIDAR-X4-USER%20Manual.pdf` but we will again list the procedure here in case itis not available. 

First you must download/clone the YDLidar-SDK repository from github. 
```bash
git clone https://github.com/YDLIDAR/YDLidar-SDK
```

once this is done you will have to compile and install the YDLidar-SDK on the RasPi with the following.
```bash
$ cd YDLidar-SDK/build
$ cmake ..
$ make
$ sudo make install
```
If this worked, the ROS driver can be installed. However before doing so, you will have download the ROS driver from github, create a catkin workspace for the ydlidar, move the ROS driver into the workspace and then compile the workspace. This can be done with the following commands. it may be beneficial to use the `ls` command to check the move was correctly exectuted before moving onto the compilation
```bash
$ cd ~
$ git clone https://github.com/YDLIDAR/ydlidar_ros_driver
$ mkdir -p ~/ydlidar_ws/src
$ mv /ydlidar_ros_driver /ydlidar_ws/src/
$ cd ~/ydlidar_ws
$ catkin_make
```
now we will add the ydlidar_ws environment to the `~/.bashrc` file:
```bash
$ echo "source ~/ydlidar_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```
and then we add a device alias to the YDLidar serial port with the command
```bash
$ cd ~/ydlidar_ws/src/ydlidar_ros_driver/startup
$ sudo chmod +x initenv.sh
$ sudo sh initenv.sh
```
one of the final steps is to install RVIZ, a 3d visualisation tool for ROS that will make it easier to view the lidar data
```bash
$ sudo apt-get install python-serial ros-kinetic-serial g++ vim \ros-kinetic-turtlebot-rviz-launchers
```
it may be possible that at this stage the installation fails. in most cases, this can be fixed by updating the source cache and then rerunning the installation, which is the following commands:
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python-serial ros-kinetic-serial g++ vim \ros-kinetic-turtlebot-rviz-launchers
```
at this point the RasPi should be ready to run the lidar. Before we get to this, you should check the connections from the lidar. on the X4 there are two micro-usb ports. look carefully on the circuit board, there will be printed usb-data on top of one port and usb-power on the other. The usb-data port should be connected directly to the RasPi. However, we found that the RasPi cannot supply the necessary power, and that if usb-power is connected to the RasPi it will recognise the lidar but return a lidar health error code. You can choose to connect the usb-power to either a normal plug or to your laptop/desktop, both options should have the necessary power for the lidar. Once done:

we can activate the lidar with
```bash
$ roslaunch ydlidar_ros_driver X4.launch
```
the lidar should now be making a big fuss and spinning. to view the data we must run RVIZ and open the correct config file. this is done by opening a new terminal tab and running the command `rviz` which will open the ROS and RVIZ software. Then to load the data click `file >> open config >> ubuntu >> ydlidar_ws >> src >> ydlidar_ros_driver >> launch >> lidar.rviz `. This will load thedata from the lidar and provide real time lidar info. 

to stop the lidar, go back to the terminal tab where you ran the `$ roslaunch ydlidar_ros_driver X4.launch` command and click ctrl-C.


