# GSoD-OSRF-Task-2021
This repository contains solutions for Google Summer of Docs (GSoD) assignment 2021. The task is about writting ROS2 nodes as publisher and subscriber to perform service-like behavior for doubling a number.

In this task, I have chosen ROS2 Foxy Fitzroy.

## Architechture
We have two nodes:

* 1st node (named -> ``Customer``): the node that publishes the number to be doubled (or for the extra task publishes two numbers to be multiplied) in ``/input`` topic. Moreover, it subscirbes to ``/result`` to get the result of the multiplication.
* 2nd node (named -> ``Multiplier``): the node that subscribes to ``/input`` topic and do the multiplication process and returns the result by publishing it to ``/result`` topic.


![Architechture](https://github.com/hany606/GSoD-OSRF-Task-2021/blob/main/assets/nodes_graph.png)

Mainly, I have implmented the nodes in 2 ways that:

First way:

* The publisher node publishes a random number (two random numbers for the extra task) every 0.5 seconds using a timer.
* The subscriber node listen to the topic and do the multiplication then publishes the result.

Second way:

* The publisher node publishes a random number (two random numbers for the extra task) and wait till it recieves a result on ``/result`` topic but if it did not recieve a result within a specific period (time-out effect), the publisher publishes with different random number as it happens if the publisher is runned but the subscriber is not runned.
* The same behavior for the subscriber node as in the first way.


## Installation and preparing the environment:

There are 2 ways to use ROS2 that I have found: normal installation or using Docker

### Normal installation:
Install ROS2 Foxy Fitzroy according to the installation section in the [documentation](https://docs.ros.org/en/foxy/Installation.html).

After the installation, you can check the following tutorials:

* [Configure environment tutorial](https://docs.ros.org/en/foxy/Tutorials/Configuring-ROS2-Environment.html).
* [Creating Workspace tutorial](https://docs.ros.org/en/foxy/Tutorials/Workspace/Creating-A-Workspace.html)
* Place the packages by copying``gsod_test_cpp``, ``gsod_test_py``, ``custom_msg_interface`` to dev_ws/src or clone the repo as in ``Creating Workspace tutorial``

### Use ROS2 through Docker

I have found this working repository and with good steps to use ROS2 Foxy Fitzroy through Docker: [repository link](https://github.com/PXLAIRobotics/ROS2FoxyDocker/blob/master/02_run_container.sh).

Then, removed lines 33 and 49 from ``02_run_container.sh`` in order not to have problems with run multiple docker continers from the same image simultanosuly.
<!-- one to run the first node  (that sends the numbers) and the other to run the second node (that multiplies the numbers)  -->

I have used the latter method to use ROS2 through Docker as I have ROS melodic and Ubutuntu 18.04 which are not compatible with ROS2 Foxy. Moreover, working using Docker is very simple and straightforward. So, I personally recommend to use this method.

After following the ``README.md`` inside the mentioned repository for docker, you may copy the packages or copy the repository inside the ``Projects`` in the cloned repository.

Full steps:

```bash
git clone https://github.com/PXLAIRobotics/ROS2FoxyDocker.git
cd ROS2FoxyDocker
./01_build_image.sh
chmod +x 01_build_image.sh
chmod +x 02_run_container_sh
```

Then, remove lines 33 and 49 from ``02_run_container.sh``

```bash 
cd Projects/dev_ws_src/ && git clone https://github.com/hany606/GSoD-OSRF-Task-2021.git
``` 
or clone it somewhere else and copy the packages directory inside ``ROS2FoxyDocker/Projects/dev_ws_src`` (This directory/volume is being accessed from inside the container)

```bash
./02_run_container.sh
cd Projects/dev_ws
```

After the installation and preparing the working space by any way, go to the working space directory and start building the packages:

Build the message interface package to avoid errors of dependencies from other packages:

```bash
colcon build --packages-select custom_msg_interface
. install/setup.bash
```
 or ``setup.zsh`` if you are using .zsh

Build the other packages:

```bash
colcon build
. install/setup.bash
```
 or ``setup.zsh`` if you are using .zsh
 
 ## Packages:


### gsod_test_py
This package contains the implementation of the task using python, it contains the following nodes:

* customer: publisher node for the 1st way as it is mentioned in the Architechture section.
* multiplier: subscriber node.

* customer_msg: publisher node for the 1st way as it is mentioned in the Architechture section but with the custom message and sends two numbers to be multiplied together.
* multiplier_msg: subscriber node.

* customerv2: publisher node for the 2nd way as it is mentioned in the Architechture section.

* customerv2_msg: publisher node for the 2nd way as it is mentioned in the Architechture section but with the custom message and sends two numbers to be multiplied together.


### gsod_test_cpp
This package contains the implementation of the task using c++

* customer: publisher node for the 1st way as it is mentioned in the Architechture section.
* multiplier: subscriber node.

* customer_msg: publisher node for the 1st way as it is mentioned in the Architechture section but with the custom message and sends two numbers to be multiplied together.
* multiplier_msg: subscriber node.


Note: I have implemented the 2nd way for the assignment only in python because I wanted just to show how the 2nd way behave and actually the code of the 1st way is not that different than 2nd way.

## How to run?

After building the packages and source the workspace, we need to open two terminals and run one for customer node and one for multiplier node.

The following command to run the node in general:
```bash
ros2 run <package-name> <node-name>
```

For example, for python-based package:

```bash
ros2 run gsod_test_py customer
```

```bash
ros2 run gsod_test_py multiplier
```

## References:
I strongly recommend to read these tutorials for more information about ROS2:

* [ROS2 documentation for creating a package](https://docs.ros.org/en/foxy/Tutorials/Creating-Your-First-ROS2-Package.html) 
* ROS2 tutorial for creating a simple publisher and subscriber in [python](https://docs.ros.org/en/foxy/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber.html) and [C++](https://docs.ros.org/en/foxy/Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)
* [ROS2 tutorial for creating a custom message](https://docs.ros.org/en/foxy/Tutorials/Custom-ROS2-Interfaces.html)

## TODO:

- [x] Add about docker: https://github.com/PXLAIRobotics/ROS2FoxyDocker/blob/master/02_run_container.sh
- [x] Add about steps and modification to run the dockerfile
- [x] Write about creating the packages
- [x] Write steps to run all the stuff
- [x] Add references
